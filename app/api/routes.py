from fastapi import APIRouter, HTTPException, Depends, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.config import settings
from app.core.endpoints import consultar_riesgo_experian
from app.core.logger import logger
from app.core.security import api_key_auth
from app.models.experian_model import ExperianJsonModel
from app.repositories.auditoria_repository import guardar_auditoria
from app.services.cliente_service import get_features
from app.services.patch_json import patch_json
from app.utils.validators import validar_cuit

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.get("/cliente/{cuit}")
@limiter.limit(settings.RATE_LIMIT)
async def cliente_endpoint(
    request: Request,
    cuit: str,
    api_key: str = Depends(api_key_auth)
):
    logger.info(f"Request CUIT: {cuit}")

    if not validar_cuit(cuit):
        raise HTTPException(status_code=400, detail="CUIT inválido")

    try:
        data = get_features(cuit)

        if not data:
            raise HTTPException(status_code=404, detail="No encontrado")

        return {
            "status": "success",
            "data": data
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="No encontrado")

@router.post("/riesgo_cliente/")
@limiter.limit(settings.RATE_LIMIT)
async def riesgo_cliente_endpoint(
    request: Request,
    body: ExperianJsonModel,
    api_key: str = Depends(api_key_auth)
):
    cuit = body.DAJSONDocumentV2.Input.Clientes.Datos_Personales.Persona_humana.Id_persona
    logger.info(f"Request CUIT: {body.DAJSONDocumentV2.Input.Clientes.Datos_Personales.Persona_humana.Id_persona}")

    if not validar_cuit(cuit):
        raise HTTPException(status_code=400, detail="CUIT inválido")

    try:
        data = get_features(cuit)

        if not data:
            raise HTTPException(status_code=404, detail="No encontrado")

        data = data.model_dump(exclude_unset=True)
        body = body.model_dump()
        result = patch_json(body, data)
        response = await consultar_riesgo_experian(result)

        guardar_auditoria( cuit, 'OK', result, response)

        return {
            "status": "success",
            "data": response
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error: {e}")
        guardar_auditoria( cuit, 'ERROR', result, response)
        raise HTTPException(status_code=500, detail="No encontrado")
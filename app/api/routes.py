from fastapi import APIRouter, HTTPException, Depends, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.config import settings
from app.core.endpoints import consultar_riesgo_experian
from app.core.logger import logger
from app.core.security import api_key_auth
from app.models.experian_model import ExperianJsonModel
from app.repositories.auditoria_repository import guardar_auditoria
from app.repositories.cliente_repository import upsert_experian_data
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

        #GET -> COMPARO CONTRA FRONT -> INSERT -> EXPERIAN
        data = get_features(cuit)

        if not data:
            raise HTTPException(status_code=404, detail="No encontrado")
        data = data.model_dump(exclude_unset=True)
        print('DATA', data)
        body = body.model_dump()

        #REVISAR PARA SOLO PISAR LOS CASOS NULOS O VACIOS EN EL BODY!!!!!!!!!!!!!!!!!!!

        body["DAJSONDocumentV2"]["Input"] = patch_json(body["DAJSONDocumentV2"]["Input"], data)
        #INSERT OR UPDATE
        print('Input', body["DAJSONDocumentV2"]["Input"])
        upsert_experian_data(body["DAJSONDocumentV2"]["Input"])
        response = await consultar_riesgo_experian(body)
        guardar_auditoria( cuit, 'OK', body, response)
        return {
            "status": "success",
            "data": response
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error: {e}")
        #VALIDAR QUE EL RESPONSE este sino validar response
        guardar_auditoria( cuit, 'ERROR', body, e)
        raise HTTPException(status_code=500, detail="No encontrado")
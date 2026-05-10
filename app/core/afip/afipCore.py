import os
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder

from app.core.afip.auth import login
from app.core.afip.padron import consultar_padron, transformar_respuesta
from app.core.afip.token_manager import cargar_token, guardar_token

load_dotenv()

CUIT_REPRESENTADA = os.getenv("CUIT_REPRESENTADA")

async def cargar_info_afip(cuit):
    token, sign = await cargar_token()

    if not token:
        token, sign, expiration = await login()
        guardar_token(token, sign, expiration)

    resp = await consultar_padron(token, sign, CUIT_REPRESENTADA, cuit)
    data = transformar_respuesta(resp)
    datos_limpios = jsonable_encoder(data)
    return datos_limpios
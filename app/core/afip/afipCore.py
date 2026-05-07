import os
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder

from app.core.afip.auth import login
from app.core.afip.padron import consultar_padron, transformar_respuesta
from app.core.afip.token_manager import cargar_token, guardar_token

load_dotenv()

CUIT_REPRESENTADA = os.getenv("CUIT_REPRESENTADA")

async def cargar_info_afip(cuit):
   # print("🔐 Autenticando con AFIP...")
   # token, sign = login()
    token, sign = await cargar_token()

    if not token:
        print("🔐 Generando nuevo token")
        token, sign, expiration = await login()
        guardar_token(token, sign, expiration)
    else:
        print("♻️ Reutilizando token")

    print("📡 Consultando padrón A5...")
    resp = await consultar_padron(token, sign, CUIT_REPRESENTADA, cuit)
    print(resp)
    data = transformar_respuesta(resp)


    datos_limpios = jsonable_encoder(data)
    print("\n✅ Resultado:")
    print(datos_limpios)
    return datos_limpios
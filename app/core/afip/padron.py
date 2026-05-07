from zeep import Client
from zeep.helpers import serialize_object

PADRON_URL = "https://aws.afip.gov.ar/sr-padron/webservices/personaServiceA5?wsdl"


async def consultar_padron(token, sign, cuit_rep, cuit_consulta):
    client = Client(PADRON_URL)

    response = client.service.getPersona(
        token=token,
        sign=sign,
        cuitRepresentada=cuit_rep,
        idPersona=cuit_consulta
    )

    return response


def transformar_respuesta(resp):
    try:
        data = serialize_object(resp)
        return data
    except Exception as e:
        return {
            "error": "No se pudo parsear respuesta",
            "detalle": str(e)
        }
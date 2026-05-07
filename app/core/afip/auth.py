import os
import base64
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, UTC
from zeep import Client
from dotenv import load_dotenv

load_dotenv()

CERT = os.getenv("CERT_PATH")
KEY = os.getenv("KEY_PATH")

WSAA_URL =  "https://wsaa.afip.gov.ar/ws/services/LoginCms?wsdl"



def crear_tra():
    now = datetime.now(UTC)
    print("LOCAL:", datetime.now())
    print("UTC:", datetime.now(UTC))
    generation = (now - timedelta(minutes=10)).strftime('%Y-%m-%dT%H:%M:%SZ')
    expiration = (now + timedelta(minutes=10)).strftime('%Y-%m-%dT%H:%M:%SZ')

    tra = f"""<?xml version="1.0" encoding="UTF-8"?>
<loginTicketRequest version="1.0">
    <header>
        <uniqueId>{int(now.timestamp())}</uniqueId>
        <generationTime>{generation}</generationTime>
        <expirationTime>{expiration}</expirationTime>
    </header>
    <service>ws_sr_padron_a5</service>
</loginTicketRequest>"""

    return tra


def firmar_tra(tra_xml):
    with open("tra.xml", "w", encoding="utf-8", newline="\n") as f:
        f.write(tra_xml.strip())

    cmd = (
        f"openssl smime -sign "
        f"-signer {CERT} "
        f"-inkey {KEY} "
        f"-outform DER -md SHA256 -binary -nodetach "
        f"-in tra.xml -out tra.cms"
    )

    subprocess.run(cmd, shell=True, check=True)

    with open("tra.cms", "rb") as f:
        cms_bin = f.read()
    cms_base64 = base64.b64encode(cms_bin).decode("utf-8")

    return cms_base64


async def login():
    tra = crear_tra()
    print("TRA A ENVIAR:\n", tra)
    cms = firmar_tra(tra)

    client = Client(WSAA_URL)
    response = client.service.loginCms(cms)

    root = ET.fromstring(response)
    token = root.find(".//token").text

    sign = root.find(".//sign").text
    expirationTime = root.find(".//expirationTime").text

    return token, sign, expirationTime
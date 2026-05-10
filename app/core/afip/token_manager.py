import json
from datetime import datetime, timedelta

TOKEN_FILE = "./afip_token.json"


def guardar_token(token, sign, expiration):
    with open(TOKEN_FILE, "w") as f:
        json.dump({
            "token": token,
            "sign": sign,
            "expiration": expiration
        }, f)


async def cargar_token():
    try:
        with open(TOKEN_FILE, "r") as f:
            data = json.load(f)
        exp_str = data["expiration"]
        if exp_str.endswith("Z"):
            exp_str = exp_str.replace("Z", "")
        else:
            exp_str = exp_str[:-6]  # corta "-03:00"

        exp = datetime.fromisoformat(exp_str)
        if datetime.utcnow() < (exp - timedelta(minutes=5)):
            return data["token"], data["sign"]

        return None, None

    except Exception as e:
        print("Error leyendo token:", e)
        return None, None
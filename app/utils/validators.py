import re

def validar_cuit(cuit: str) -> bool:
    return bool(re.match(r'^\d{11}$', cuit))
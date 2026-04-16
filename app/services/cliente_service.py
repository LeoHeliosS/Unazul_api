from app.repositories.cliente_repository import fetch_features

def get_features(cuit: str):
    data = fetch_features(cuit)

    print("DATA EN SERVICE:", data)
    print("TYPE:", type(data))

    if not data:
        print("ENTRÓ AL IF ❌")
        raise Exception("Cliente no encontrado")

    print("SALE OK ✅")

    return  data
import httpx


async def consultar_riesgo_experian(body: dict):
    url = "http://10.19.110.30:8092/DAServiceJSON"
    headers = {}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=body, headers=headers)

        # Levanta una excepción si hay error (4xx o 5xx)
        response.raise_for_status()
        print(response)
        return response.json()
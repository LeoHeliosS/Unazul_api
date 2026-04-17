from app.db import get_connection, release_connection
#from app.models.cliente_model import Cliente, DatosImpositivos, Afip
from app.services.definition_map import mapear_fila_a_cliente

def fetch_features(cuit: str):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT *
        FROM ops.entrada_experian
        WHERE id_persona = %s
    """

    cursor.execute(query, (cuit,))
    row = cursor.fetchone()
    print("ROW:", row)
    if not row:
        return None

    columns = [desc[0] for desc in cursor.description]

    result = dict(zip(columns, row))
    print("RESULT:", result)
    cliente_json = mapear_fila_a_cliente(result)

    cursor.close()
    release_connection(conn)
    return cliente_json#.model_dump_json(indent=4)#result

#def fetch_cliente(cuit: str):
 #   return ("a","b","c","d","e","f","g","h","i","j")
from app.db import get_connection, release_connection
#from app.models.cliente_model import Cliente, DatosImpositivos, Afip
from app.services.definition_map import mapear_fila_a_cliente

import json
import psycopg2
from psycopg2.extras import execute_values


def flatten_json(data, flat_dict=None):
    if flat_dict is None:
        flat_dict = {}

    for key, value in data.items():
        clean_key = key.lower()

        if isinstance(value, dict):
            flatten_json(value, flat_dict)
        elif isinstance(value, list):
            flat_dict[clean_key] = ";".join(map(str, value)) if value else None
        else:
            flat_dict[clean_key] = value

    return flat_dict

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


def upsert_experian_data(json_data):
    datos_sucios = flatten_json(json_data)
    id_persona = datos_sucios.get('id_persona')

    if not id_persona:
        print("Error: El JSON no contiene id_persona")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT 1 FROM ops.entrada_experian WHERE id_persona = %s", (id_persona,))
        existe = cursor.fetchone()
        cursor.execute("""
                       SELECT column_name
                       FROM information_schema.columns
                       WHERE table_schema = 'ops'
                         AND table_name = 'entrada_experian'
                       """)
        columnas_tabla = [row[0] for row in cursor.fetchall()]

        datos_finales = {k: v for k, v in datos_sucios.items() if k in columnas_tabla}
        columnas = list(datos_finales.keys())
        valores = [datos_finales[c] for c in columnas]

        if existe:
            print(f"Actualizando registro existente: {id_persona}")
            set_clause = ", ".join([f"{c} = %s" for c in columnas if c != "id_persona"])
            valores_update = [datos_finales[c] for c in columnas if c != "id_persona"]
            valores_update.append(id_persona)

            query_update = f"UPDATE ops.entrada_experian SET {set_clause} WHERE id_persona = %s"
            cursor.execute(query_update, valores_update)
        else:
            print(f"Insertando nuevo registro: {id_persona}")
            placeholders = ", ".join(["%s"] * len(columnas))
            columnas_sql = ", ".join(columnas)
            query_insert = f"INSERT INTO ops.entrada_experian ({columnas_sql}) VALUES ({placeholders})"
            cursor.execute(query_insert, valores)

        conn.commit()
        print(f"Proceso completado para {id_persona}")

    except Exception as e:
        conn.rollback()
        print(f"Error en Upsert Manual: {e}")
    finally:
        cursor.close()
        release_connection(conn)
#def fetch_cliente(cuit: str):
 #   return ("a","b","c","d","e","f","g","h","i","j")
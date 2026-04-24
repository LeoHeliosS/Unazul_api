import json

from app.db import get_connection, release_connection


def guardar_auditoria(cuit, estado_consulta, request_data, response_data):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
            INSERT INTO ops.auditoria (nombre_endpoint, \
                                                cuit, \
                                                estado_consulta, \
                                                request_data, \
                                                response_data) \
            VALUES (%s, %s, %s, %s, %s) \
            """

    try:
        valores = (
            "/riesgo_cliente/",
            cuit,
            estado_consulta,
            json.dumps(request_data),
            str(response_data)
        )

        cursor.execute(query, valores)

        conn.commit()
        print("Auditoría guardada exitosamente.")

    except Exception as e:
        conn.rollback()
        print(f"Error al insertar auditoría: {e}")

    finally:
        cursor.close()
        release_connection(conn)


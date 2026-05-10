from app.models.cliente_model import *


def normalizar_para_pydantic(modelo_cls, datos_planos: dict):
    datos_normalizados = {}
    config_relleno = {
        "Id_entidades_deuda": {"longitud": 25, "defecto": "000"},
        "Sit_deuda_entidades": {"longitud": 25, "defecto": "11"},
        "Mto_deuda_entidades": {"longitud": 25, "defecto": 0}
    }
    for nombre_campo, info_campo in modelo_cls.model_fields.items():
        valor = datos_planos.get(nombre_campo.lower())
        if isinstance(valor, str) and ';' in valor:
            try:
                valor = [x.strip() for x in valor.split(';') if x.strip()]
            except ValueError:
                pass
        es_tipo_lista = "List" in str(info_campo.annotation) or "list" in str(info_campo.annotation)
        if es_tipo_lista:
            if valor in [None, '0', 0, '']:
                lista_temp = []
            elif not isinstance(valor, list):
                lista_temp = [valor]
            else:
                lista_temp = valor

            if nombre_campo in config_relleno:
                conf = config_relleno[nombre_campo]
                actual = lista_temp[:conf["longitud"]]
                faltantes = conf["longitud"] - len(actual)
                datos_normalizados[nombre_campo] = actual + [conf["defecto"]] * faltantes
            else:
                datos_normalizados[nombre_campo] = lista_temp
        else:
            datos_normalizados[nombre_campo] = valor

    return datos_normalizados

def normalizar_fila_individual(fila_db):

    val_tipo_cliente = fila_db

    if val_tipo_cliente in [None, '0', 0, '']:
        id_tipo_cliente_final = []
    elif not isinstance(val_tipo_cliente, list):
        if isinstance(val_tipo_cliente, str) and ';' in val_tipo_cliente:
            id_tipo_cliente_final = [x.strip() for x in val_tipo_cliente.split(';') if x.strip()]
        else:
            id_tipo_cliente_final = [val_tipo_cliente]
    else:
        id_tipo_cliente_final = val_tipo_cliente

    return id_tipo_cliente_final

def mapear_json_a_afip_model(json_data: dict) -> AfipModel:
    dg = json_data.get("datosGenerales") or {}
    dm = json_data.get("datosMonotributo") or {}
    drg = json_data.get("datosRegimenGeneral") or {}

    actividad_mono = dm.get("actividadMonotributista") if dm else None
    lista_actividades_rg = drg.get("actividad", [])
    actividad_rg = lista_actividades_rg[0] if lista_actividades_rg else {}

    actividad_obj = actividad_mono or actividad_rg
    id_actividad = actividad_obj.get("idActividad") or actividad_obj.get("idActivity")

    cat_mono = dm.get("categoriaMonotributo") or {}

    impuestos_rg = drg.get("impuesto", [])

    info_iva = next((i for i in impuestos_rg if i.get("idImpuesto") == 30), {})
    info_gan = next((i for i in impuestos_rg if i.get("idImpuesto") in [10, 11]), {})
    data_mapeada = {
        "Id_categoria_monotributo": str(cat_mono.get("idCategoria", "")),
        "Fecha_inscripcion_monotributo": cat_mono.get("periodo"),
        "Es_autonomo": 1 if drg.get("categoriaAutonomo") else 0,
        "Fecha_inscripcion_autonomo": drg.get("periodo") if drg else None,
        "Id_actividad_principal": id_actividad,
        "Actividad_monotributista": actividad_obj.get("descripcionActividad"),
        "Id_iva_inscripto": info_iva.get("estadoImpuesto", ""),
        "Id_ig_inscripto": info_gan.get("estadoImpuesto", ""),
        "Fecha_alta_iva": info_iva.get("periodo", 0),
        "Fecha_alta_ganancias": info_gan.get("periodo", 0),
        "Es_sucesion": dg.get("esSucesion", "NO"),
        "Categoria_autonomo": drg.get("categoriaAutonomo"),

        # --- CAMPOS FALTANTES PARA EVITAR EL VALIDATION ERROR ---
        "Tuvo_cambio_categoria": 0,
        "Tuvo_cambio_categoria_ult_6m": 0,
        "Tuvo_cambio_categoria_ult_12m": 0,
        "Tuvo_cambio_categoria_ult_18m": 0,
        "Signo_cambio_categoria": 0,
        "Id_actividad_secundaria": 0,
        "Id_actividad_tercera": 0,
        "Fecha_actividad_principal": actividad_obj.get("periodo", "0") # Usamos el periodo de la actividad encontrada?
    }

    return AfipModel(**data_mapeada)
def mapear_fila_a_cliente(fila_db: dict, afip_json) -> InputModel:

    #datos_afip = normalizar_para_pydantic(AfipModel, fila_db)
    datos_bcra = normalizar_para_pydantic(Bcra, fila_db)
    datos_persona = normalizar_para_pydantic(PersonaHumana, fila_db)
    datos_aml = normalizar_para_pydantic(Aml, fila_db)
    datos_acredita = normalizar_para_pydantic(AcreditaHaberes, fila_db)
    datos_anses = normalizar_para_pydantic(Anses, fila_db)
    datos_bcra_cr = normalizar_para_pydantic(Bcra_cr, fila_db)
    datos_cheques = normalizar_para_pydantic(Cheques, fila_db)
    datos_veraz = normalizar_para_pydantic(Veraz, fila_db)
    datos_perfil = normalizar_para_pydantic(Perfil, fila_db)
    datos_compra_cartera = normalizar_para_pydantic(Compra_De_Cartera, fila_db)
    datos_limpieza_haberes = normalizar_para_pydantic(Limpieza_De_Haberes, fila_db)
    datos_refinanciaciones = normalizar_para_pydantic(Refinanciaciones, fila_db)
    datos_reprogramados = normalizar_para_pydantic(Reprogramados, fila_db)
    datos_cuenta_sueldo = normalizar_para_pydantic(Cuenta_Sueldo, fila_db)
    datos_caja_ahorro = normalizar_para_pydantic(Caja_De_Ahorro, fila_db)
    datos_cuenta_corriente = normalizar_para_pydantic(Cuenta_Corriente, fila_db)
    datos_plazo_fijo = normalizar_para_pydantic(Plazo_Fijo, fila_db)
    datos_tarjetas = normalizar_para_pydantic(Tarjetas, fila_db)
    datos_homebanking = normalizar_para_pydantic(Home_Banking, fila_db)
    datos_ant_negativo = normalizar_para_pydantic(Ant_negativo, fila_db)
    datos_morosidad = normalizar_para_pydantic(Morosidad, fila_db)
    datos_bases_externas = normalizar_para_pydantic(Basesexternas, fila_db)
    datos_filler = normalizar_para_pydantic(Filler, fila_db)
    fecha_raw = fila_db.get("fecha_alta_cliente")
    if fecha_raw:
        Fecha_alta_cliente = fecha_raw.strftime('%Y%m%d')
    else:
        Fecha_alta_cliente = "19000101"

    # Construimos la estructura anidada
    return InputModel(
        Clientes=Clientes(
            Datos_Impositivos=DatosImpositivos(
                Afip=mapear_json_a_afip_model(afip_json)
            ),
            Datos_Personales=DatosPersonales(
                Aml=Aml(**datos_aml),
                Persona_humana = PersonaHumana(**datos_persona)
            ),
            Perfil_Tecnico=PerfilTecnico(
                Acredita_haberes=AcreditaHaberes(**datos_acredita),
                Anses = Anses(**datos_anses),
                Bcra = Bcra(**datos_bcra),
                Bcra_cr=Bcra_cr(**datos_bcra_cr),
                Cheques=Cheques(**datos_cheques),
                Veraz=Veraz(**datos_veraz),
                Id_tipo_cliente=normalizar_fila_individual(fila_db.get('id_tipo_cliente')),
                Fecha_alta_cliente=Fecha_alta_cliente,
                Id_banco_cuenta=fila_db.get("id_banco_cuenta"),
                Id_segmento_comercial=fila_db.get("id_segmento_comercial"),
                Id_cartera_comercial=fila_db.get("id_cartera_comercial"),
                Id_sucursal_origen=fila_db.get("id_sucursal_origen"),
                Id_provincia=fila_db.get("id_provincia"),
                Score_nosis_empleador=fila_db.get("score_nosis_empleador"),
                Perfil=Perfil(**datos_perfil)
            ),
            Tipo_proceso = fila_db.get("tipo_proceso")
        ),
        Productos=Productos(
            Prestamos = Prestamos(
                Adelanto_haberes = Adelanto_haberes(
                    Mto_adelanto_haberes = fila_db.get("mto_adelanto_haberes")
                ),
                Compra_De_Cartera = Compra_De_Cartera(**datos_compra_cartera),
                Limpieza_De_Haberes=Limpieza_De_Haberes(**datos_limpieza_haberes),
                Refinanciaciones=Refinanciaciones(**datos_refinanciaciones),
                Reprogramados=Reprogramados(**datos_reprogramados),
                Mto_deuda_pp_vigente = normalizar_fila_individual(fila_db.get("mto_deuda_pp_vigente")),
                Nro_cuota_pp_vigente = normalizar_fila_individual(fila_db.get("nro_cuota_pp_vigente")),
                Fecha_alta_pp_vigente = normalizar_fila_individual(fila_db.get("fecha_alta_pp_vigente")),
                Q_cuotas_total = normalizar_fila_individual(fila_db.get("q_cuotas_total")),
                Q_cuotas_pagas = normalizar_fila_individual(fila_db.get("q_cuotas_pagas")),
                Mto_cuota_debit_haberes = normalizar_fila_individual(fila_db.get("mto_cuota_debit_haberes")),
                Mto_cuota_vigente = normalizar_fila_individual(fila_db.get("mto_cuota_vigente")),
                Capital_origen_pp = normalizar_fila_individual(fila_db.get("capital_origen_pp")),
                Mto_cuota_vigente_gp = normalizar_fila_individual(fila_db.get("mto_cuota_vigente_gp")),
                Nro_linea_prestamo = normalizar_fila_individual(fila_db.get("nro_linea_prestamo")),
                Id_destino_fondos = normalizar_fila_individual(fila_db.get("id_destino_fondos")),
                Dias_mora_linea_prestamo = fila_db.get("dias_mora_linea_prestamo"),
                Mto_prestamo_total = fila_db.get("mto_prestamo_total"),
                Cuota_mto_prestamo_total = fila_db.get("cuota_mto_prestamo_total"),
                Mto_cuota_debit_haberes_mes_1 = fila_db.get("mto_cuota_debit_haberes_mes_1"),
                Mto_cuota_debit_haberes_mes_2 = fila_db.get("mto_cuota_debit_haberes_mes_2"),
                Mto_cuota_debit_haberes_mes_3 = fila_db.get("mto_cuota_debit_haberes_mes_3"),
                Mto_cuota_vigente_mes_1 = fila_db.get("mto_cuota_vigente_mes_1"),
                Mto_cuota_vigente_mes_2 = fila_db.get("mto_cuota_vigente_mes_2"),
                Mto_cuota_vigente_mes_3 = fila_db.get("mto_cuota_vigente_mes_3")
            ),
            Cuenta_Sueldo = Cuenta_Sueldo(**datos_cuenta_sueldo),
            Q_Productos_Vigentes = fila_db.get("q_productos_vigentes"),
            Q_Lineas_Producto_Vigentes = fila_db.get("q_lineas_producto_vigentes"),
            Q_Productos_Credito_GP = fila_db.get("q_productos_credito_gp"),
            Caja_De_Ahorro = Caja_De_Ahorro(**datos_caja_ahorro),
            Cuenta_Corriente = Cuenta_Corriente(**datos_cuenta_corriente),
            Plazo_Fijo = Plazo_Fijo(**datos_plazo_fijo),
            Tarjetas  = Tarjetas(**datos_tarjetas)
        ),
        Solicitud = Solicitud(
            Canal_soli_producto = fila_db.get("canal_soli_producto")
        ),
        Canales_Y_Gestiones = Canales_Y_Gestiones(
            Home_Banking = Home_Banking(**datos_homebanking)
        ),
        Riesgos=Riesgos(
            Antecedentes_Negativos = Antecedentes_Negativos(
                Ant_negativo=Ant_negativo(**datos_ant_negativo)
            ),
            Mora=Mora(
                Morosidad=Morosidad(**datos_morosidad)
            ),
            Id_corrida= fila_db.get("id_corrida"),
            Ult_fecha_eval_motor= fila_db.get("ult_fecha_eval_motor"),
            Fecha_vencimiento_calif= fila_db.get("fecha_vencimiento_calif"),
            Ult_fecha_calificacion_aprobada= fila_db.get("ult_fecha_calificacion_aprobada"),
            Mto_pp_ult_calif= fila_db.get("mto_pp_ult_calif"),
            Fecha_mto_pp_ult_calif= fila_db.get("fecha_mto_pp_ult_calif"),
            Mto_visa_ultima_calif= fila_db.get("mto_visa_ultima_calif"),
            Fecha_mto_visa_ult_calif= fila_db.get("fecha_mto_visa_ult_calif"),
            Mto_master_ult_calif= fila_db.get("mto_master_ult_calif"),
            Fecha_mto_master_ult_calif= fila_db.get("fecha_mto_master_ult_calif"),
            Mto_acuerdo_ult_calif= fila_db.get("mto_acuerdo_ult_calif"),
            Fecha_mto_acuerdo_ult_calif= fila_db.get("fecha_mto_acuerdo_ult_calif"),
            Mto_adelanto_haberes_ult_calif= fila_db.get("mto_adelanto_haberes_ult_calif"),
            Fecha_mto_adelanto_haberes_ult_calif= fila_db.get("fecha_mto_adelanto_haberes_ult_calif"),
            Mto_upgrade_master_ult_calif= fila_db.get("mto_upgrade_master_ult_calif"),
            Fecha_mto_upgrade_master_ult_calif= fila_db.get("fecha_mto_upgrade_master_ult_calif"),
            Mto_upgrade_visa_ult_calif= fila_db.get("mto_upgrade_visa_ult_calif"),
            Fecha_mto_upgrade_visa_ult_calif= fila_db.get("fecha_mto_upgrade_visa_ult_calif"),
        ),
        Filler1 = fila_db.get("filler1"),
        Filler2 = fila_db.get("filler2"),
        Filler3 = fila_db.get("filler3"),
        Filler4 = fila_db.get("filler4"),
        Filler5 = fila_db.get("filler5"),
        Date1 = fila_db.get("date1"),
        Date2 = fila_db.get("date2"),
        Date3 = fila_db.get("date3"),
        Date4 = fila_db.get("date4"),
        Date5 = fila_db.get("date5"),
        Decimal1 = fila_db.get("decimal1"),
        Decimal2 = fila_db.get("decimal2"),
        Decimal3 = fila_db.get("decimal3"),
        Decimal4 = fila_db.get("decimal4"),
        Decimal5 = fila_db.get("decimal5"),
        Campanias=Campanias(
            Campanas=Campanas(
                Basesexternas=Basesexternas(**datos_bases_externas)
            )
        ),
        Filler = Filler(**datos_filler)
    )



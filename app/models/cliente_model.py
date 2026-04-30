from datetime import date
from typing import Optional, List, Any

from pydantic import BaseModel, field_validator, ConfigDict





class Basesexternas(BaseModel):
    Politica_riesgo: Optional[str]
    Segmento_riesgos: Optional[str]
    Mto_haber_informado_empleador: Optional[int]
    Ponderador: Optional[str]
    Codigo_limite_visa: Optional[str]
    Cuit_informado_empleador: Optional[str]
    Nombre_informado_empleador: Optional[str]
    Banco_calificador: Optional[str]
    Politica_credito: Optional[str]
    Descripcion_base: Optional[str]

class AfipModel(BaseModel):
    Id_categoria_monotributo: Optional[str]
    Fecha_inscripcion_monotributo: Optional[int]
    Es_autonomo: Optional[int]
    Fecha_inscripcion_autonomo: Optional[int]
    Tuvo_cambio_categoria_ult_6m: Optional[int]
    Tuvo_cambio_categoria_ult_12m: Optional[int]
    Tuvo_cambio_categoria_ult_18m: Optional[int]
    Signo_cambio_categoria: Optional[int]
    Tuvo_cambio_categoria: Optional[int]
    Id_actividad_principal: Optional[int]
    Id_actividad_secundaria: Optional[int]
    Id_actividad_tercera: Optional[int]
    Fecha_actividad_principal: Optional[int]
    Id_iva_inscripto: Optional[str]
    Id_ig_inscripto: Optional[str]
    Fecha_alta_iva: Optional[int]
    Fecha_alta_ganancias: Optional[int]
    Es_sucesion: Optional[str]
    Categoria_autonomo: Optional[str]
    Actividad_monotributista: Optional[str]

class Aml(BaseModel):
    Es_pep: Optional[int]
    Es_vinculado: Optional[int]
    Es_sujeto_obligado: Optional[int]
    Es_fatca: Optional[int]

class PersonaHumana(BaseModel):
    Id_persona: Optional[str]
    Denominacion_persona: Optional[str]
    Fecha_nacimiento: Optional[str]
    Edad: Optional[int]
    Sexo: Optional[str]
    Id_estado_civil: Optional[str]
    Id_nacionalidad: Optional[str]
    Es_fallecido: Optional[int]

    @field_validator('Fecha_nacimiento', mode='before')
    def convertir_a_string(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

class AcreditaHaberes(BaseModel):
    Mto_haber_acreditado: Optional[List[float]]
    Mto_haber_acreditado_mes_1: Optional[List[float]]
    Mto_haber_acreditado_mes_2: Optional[List[float]]
    Mto_haber_acreditado_mes_3: Optional[List[float]]
    Mto_prom_haberes_acreditados_trim: Optional[float]
    Acredita_haberes: Optional[int]
    Cuit_empleador: Optional[List[str]]
    Id_actividad_empleado: Optional[str]
    Id_sector_empleador: Optional[str]
    Mto_prom_haberes_acreditados_trim_gp: Optional[int]
    Mto_haber_acreditado_gp: Optional[int]
    Fecha_ult_hab_acreditado: Optional[List[str]]
    Id_convenio: Optional[List[str]]
    Rel_ingreso_mensual_imvym: Optional[int]

class Anses(BaseModel):
    Nro_beneficio_anses: Optional[List[str]]
    Mto_beneficio_anses: Optional[List[float]]

class Bcra(BaseModel):
    Q_entidades_gr1: Optional[int]
    Q_entidades_gr2: Optional[int]
    Q_entidades_gr3: Optional[int]
    Q_entidades_gr4: Optional[int]
    Q_entidades_deuda: Optional[int]
    Q_entidades_sit_mayor_a_1: Optional[int]
    Max_sit: Optional[int]
    Max_sit_3m: Optional[int]
    Max_sit_6m: Optional[int]
    Max_sit_9m: Optional[int]
    Max_sit_12m: Optional[int]
    Por_deuda_bcos_gr1: Optional[int]
    Por_deuda_bcos_gr2: Optional[int]
    Por_deuda_bcos_gr3: Optional[int]
    Por_deuda_bcos_gr4: Optional[int]
    Mto_deuda_sit_mayor_a_1: Optional[int]
    Mto_deuda_sit_mayor_a_1_3m: Optional[int]
    Mto_deuda_sit_mayor_a_1_6m: Optional[int]
    Mto_deuda_sit_mayor_a_1_9m: Optional[int]
    Mto_deuda_sit_mayor_a_1_12m: Optional[int]
    Mto_deuda_total: Optional[int]
    Mto_deuda_total_2m: Optional[int]
    Mto_deuda_total_3m: Optional[int]
    Mto_deuda_total_6m: Optional[int]
    Mto_deuda_total_9m: Optional[int]
    Mto_deuda_total_12m: Optional[int]
    Mto_deuda_total_gp: Optional[int]
    Mto_deuda_total_gp_3m: Optional[int]
    Mto_deuda_total_gp_6m: Optional[int]
    Mto_deuda_total_gp_9m: Optional[int]
    Mto_deuda_total_gp_12m: Optional[int]
    Es_marca_endeudamiento: Optional[int]
    Id_entidades_deuda: Optional[List[str]]
    Sit_deuda_entidades: Optional[List[str]]
    Mto_deuda_entidades: Optional[List[float]]
    Es_marca_moroso_ex: Optional[int]

class Bcra_cr(BaseModel):
    Mto_cheq_rech_vicios_formales: Optional[int]
    Q_cheq_rech_vicios_formales: Optional[int]
    Q_cheq_rech_sf_pagos: Optional[int]
    Mto_cheq_rech_sf_pagos: Optional[int]
    Q_cheq_rech_sf_impagos: Optional[int]
    Q_cheq_rech_sf_impagos_6m: Optional[int]
    Q_cheq_rech_sf_impagos_9m: Optional[int]
    Q_cheq_rech_sf_impagos_12m: Optional[int]
    Mto_cheq_rech_sf_impagos: Optional[int]
    Mto_cheq_rech_sf_impagos_6m: Optional[int]
    Mto_cheq_rech_sf_impagos_9m: Optional[int]
    Mto_cheq_rech_sf_impagos_12m: Optional[int]

class Cheques(BaseModel):
    Q_cheq_rech_bco_vicios_formales: Optional[int]
    Mto_cheq_rech_bco_vicios_formales: Optional[int]
    Q_cheq_rech_bco_sf_impagos: Optional[int]
    Q_cheq_rech_bco_sf_impagos_6m: Optional[int]
    Q_cheq_rech_bco_sf_impagos_12m: Optional[int]
    Q_cheq_rech_bco_sf_impagos_24m: Optional[int]
    Mto_cheq_rech_bco_sf_impagos: Optional[int]
    Mto_cheq_rech_bco_sf_impagos_6m: Optional[int]
    Mto_cheq_rech_bco_sf_impagos_12m: Optional[int]
    Mto_cheq_rech_bco_sf_impagos_24m: Optional[int]
    Q_cheq_rech_bco_sf_pagos: Optional[int]
    Q_cheq_rech_bco_sf_pagos_6m: Optional[int]
    Q_cheq_rech_bco_sf_pagos_12m: Optional[int]
    Q_cheq_rech_bco_sf_pagos_24m: Optional[int]
    Mto_cheq_rech_bco_sf_pagos: Optional[int]
    Mto_cheq_rech_bco_sf_pagos_6m: Optional[int]
    Mto_cheq_rech_bco_sf_pagos_12m: Optional[int]
    Mto_cheq_rech_bco_sf_pagos_24m: Optional[int]

class Veraz(BaseModel):
    Vz_nro_cuil: Optional[str]
    Vz_dto_validado: Optional[int]
    Vz_score_riesgo: Optional[int]
    Vz_score_poblacion: Optional[str]
    Vz_geonse: Optional[str]
    Vz_edad: Optional[int]
    Vz_sexo: Optional[str]
    Vz_nombre_apellido: Optional[str]
    Vz_validacion_identidad: Optional[str]
    Vz_obra_social_titular: Optional[str]
    Vz_cat_monotributo: Optional[str]
    Vz_actividad_autonomos: Optional[str]
    Vz_marca_actividad: Optional[str]
    Vz_income_predictor: Optional[str]
    Vz_cp: Optional[str]
    Vz_q_productos_sit_2_bcra: Optional[str]
    Vz_q_productos_sit_2_bcra_ult_60m: Optional[str]
    Vz_q_meses_desde_ult_sit_mayor_igual_2: Optional[str]
    Vz_q_antiguedad_meses_tc_activa: Optional[str]
    Vz_q_prestamos_activos: Optional[str]
    Vz_max_saldo_mto_pp_ult_3m: Optional[str]
    Vz_q_cons_dist_ent_ult_12m: Optional[str]
    Vz_q_meses_ult_cons_financiera: Optional[str]
    Vz_q_meses_ult_cons_tec: Optional[str]
    Vz_q_cons_fin_ult_6m: Optional[str]
    Vz_actividad_empleador: Optional[str]
    Vz_q_meses_desde_ult_sit_2: Optional[str]
    Vz_max_limite_tc: Optional[str]
    Vz_grupo_bco_max_limite_tc: Optional[str]
    Vz_compromiso_pp_tc: Optional[str]
    Vz_cap_activ_autonomos: Optional[str]
    Vz_cons_ult_6m: Optional[str]
    Vz_cap_activ_empleador: Optional[str]
    Vz_prod_sit_bcra_mayor_a_1_ult_60m: Optional[str]
    Vz_pre_saldos_total_activas_ult_3m: Optional[str]
    Vz_suma_lim_compra_tc_ult_6m: Optional[str]
    Vz_tarjeta_saldo_suma: Optional[str]
    Vz_bureau_tarjetas_saldo_maximo_ult_12m: Optional[str]
    Vz_fecha_actualizacion: Optional[str]
    @field_validator('Vz_fecha_actualizacion', mode='before')
    def convertir_a_string(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v
    Vz_ult_modelo_actualizado: Optional[str]

class Perfil(BaseModel):
    Id_tipo_cliente_mes_1: Optional[list[str]]
    Id_tipo_cliente_mes_2: Optional[list[str]]
    Id_tipo_cliente_mes_3: Optional[list[str]]
    Es_socio: Optional[int]
    Es_socio_mto_presunto: Optional[int]
    Es_socio_segmento_ccial: Optional[str]

class PerfilTecnico(BaseModel):
    Acredita_haberes: Optional[AcreditaHaberes]
    Anses: Anses
    Bcra: Bcra
    Bcra_cr: Bcra_cr
    Cheques: Cheques
    Veraz: Veraz
    Id_tipo_cliente: Optional[List[str]]
    Fecha_alta_cliente: Optional[str]

    @field_validator('Fecha_alta_cliente', mode='before')
    def convertir_a_string(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

    Id_banco_cuenta: Optional[int]
    Id_segmento_comercial: Optional[str]
    Id_cartera_comercial: Optional[str]
    Id_sucursal_origen: Optional[int]
    Id_provincia: Optional[int]
    Score_nosis_empleador: Optional[int]
    Perfil: Perfil

# 2. Módulo de Productos
# ----------------------------------------------------------------

class Adelanto_haberes(BaseModel):
    Mto_adelanto_haberes: Optional[int]

class Compra_De_Cartera(BaseModel):
    Es_pp_vigente_ccart: Optional[int]
    Capital_origen_ccart: Optional[int]
    Fecha_alta_ccart_vigente: Optional[str]
    @field_validator('Fecha_alta_ccart_vigente', mode='before')
    def convertir_a_string(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

    Mto_deuda_ccart_vigente: Optional[int]
    Nro_cuota_ccart_vigente: Optional[int]
    Q_cuotas_total_ccart: Optional[int]
    Q_cuotas_pagas_ccart: Optional[int]
    Mto_cuota_vigente_ccart: Optional[int]

class Limpieza_De_Haberes(BaseModel):
    Es_limpieza_haberes: Optional[int]
    Capital_origen_lh: Optional[int]
    Fecha_alta_lh_vigente: Optional[str]
    Mto_deuda_lh_vigente: Optional[int]
    Nro_cuota_lh_vigente: Optional[int]
    Q_cuotas_total_lh: Optional[int]
    Q_cuotas_pagas_lh: Optional[int]
    Mto_cuota_vigente_lh: Optional[int]

class Refinanciaciones(BaseModel):
    Es_pp_vigente_refi: Optional[int]
    Capital_Origen_Refi: Optional[int]
    Fecha_alta_refi_vigente: Optional[str]
    Mto_deuda_refi_vigente: Optional[int]
    Nro_cuota_refi_vigente: Optional[int]
    Q_cuotas_total_refi: Optional[int]
    Q_cuotas_pagas_refi: Optional[int]
    Mto_cuota_vigente_refi: Optional[int]

class Reprogramados(BaseModel):
    Capital_origen_repro: Optional[int]
    Fecha_alta_repro_vigente: Optional[str]
    Mto_deuda_repro_vigente: Optional[int]
    Q_cuotas_repro_vigentes: Optional[int]
    Mto_cuota_repro_vigente: Optional[int]
    Mto_deuda_repro_exigible: Optional[int]
    Mto_cuota_repro_exigible: Optional[int]

class Prestamos(BaseModel):
    Adelanto_haberes: Adelanto_haberes
    Compra_De_Cartera: Compra_De_Cartera
    Limpieza_De_Haberes: Limpieza_De_Haberes
    Refinanciaciones: Refinanciaciones
    Reprogramados: Reprogramados
    Mto_deuda_pp_vigente: Optional[list[float]]
    Nro_cuota_pp_vigente: Optional[list[int]]
    Fecha_alta_pp_vigente: Optional[list[str]]
    Q_cuotas_total: Optional[list[int]]
    Q_cuotas_pagas: Optional[list[int]]
    Mto_cuota_debit_haberes: Optional[list[float]]
    Mto_cuota_vigente: Optional[list[float]]
    Capital_origen_pp: Optional[list[float]]
    Mto_cuota_vigente_gp: Optional[list[float]]
    Nro_linea_prestamo: Optional[list[int]]
    Id_destino_fondos: Optional[list[int]]
    Dias_mora_linea_prestamo: Optional[list[int]]
    Mto_prestamo_total: Optional[float]
    Cuota_mto_prestamo_total: Optional[float]
    Mto_cuota_debit_haberes_mes_1: Optional[list[float]]
    Mto_cuota_debit_haberes_mes_2: Optional[list[float]]
    Mto_cuota_debit_haberes_mes_3: Optional[list[float]]
    Mto_cuota_vigente_mes_1: Optional[list[float]]
    Mto_cuota_vigente_mes_2: Optional[list[float]]
    Mto_cuota_vigente_mes_3: Optional[list[float]]

class Cuenta_Sueldo(BaseModel):
    Nro_cuenta_sueldo: Optional[int]
    Fecha_alta_cuenta_sueldo: Optional[str]
    Es_cuenta_sueldo: Optional[int]
    Tipo_cuenta_sueldo: Optional[str]
    Producto_cuenta_sueldo: Optional[str]

class Caja_De_Ahorro(BaseModel):
    Es_ca_activo: Optional[int]
    Saldo_ca_mes_1: Optional[int]
    Saldo_ca_mes_2: Optional[int]
    Saldo_ca_mes_3: Optional[int]

class Cuenta_Corriente(BaseModel):
    Es_cc_activo: Optional[int]
    Mto_saldo_acuerdo_cc: Optional[int]
    Mto_acuerdo_cc: Optional[int]
    Fecha_alta_acuerdo_cc: Optional[str]
    Saldo_cc_mes_1: Optional[int]
    Saldo_cc_mes_2: Optional[int]
    Saldo_cc_mes_3: Optional[int]

class Plazo_Fijo(BaseModel):
    Es_pf_activo: Optional[int]
    Monto_pf_mes_1: Optional[int]
    Monto_pf_mes_2: Optional[int]
    Monto_pf_mes_3: Optional[int]
    Monto_pf_mes_4: Optional[int]
    Monto_pf_mes_5: Optional[int]
    Monto_pf_mes_6: Optional[int]

class Tarjetas(BaseModel):
    Fecha_aumento_limite_transitorio: Optional[str]
    Nro_cuenta_tc: Optional[list[str]]
    Nro_sucursal_cuenta_tc: Optional[list[str]]
    Tipo_plastico_tc: Optional[list[str]]
    Marca_tc: Optional[list[str]]
    Mto_limite_compras_cuotas: Optional[int]
    Mto_saldo_deuda_total: Optional[int]
    Mto_abonado: Optional[list[int]]
    Es_pago_minimo: Optional[list[int]]
    Nivel_uso_tarjeta: Optional[list[int]]
    Fecha_alta_tc: Optional[list[str]]
    Fecha_aumento_limite_compra: Optional[str]
    Mto_limite_compra: Optional[list[int]]
    Tiene_plan_financiacion: Optional[int]
    Tiene_plan_financiacion_ult_12m: Optional[int]
    Tiene_plan_financiacion_ult_3m: Optional[int]
    Mto_limite_compra_gp: Optional[int]
    Mto_saldo_deuda_total_gp: Optional[int]
    Nivel_uso_tarjetas_gp: Optional[int]
    Min_nivel_uso_tarjeta_trim_gp: Optional[int]
    Max_nivel_uso_tarjeta_trim_gp: Optional[int]
    Prom_nivel_uso_tarjeta_trim_gp: Optional[int]
    Evolucion_nivel_uso_tarjeta_gp: Optional[int]
    Nivel_pago_tarjeta_gp: Optional[int]
    Mto_pago_min_mes_1: Optional[list[int]]
    Mto_pago_min_mes_2: Optional[list[int]]
    Mto_pago_min_mes_3: Optional[list[int]]
    Mto_pago_min_mes_4: Optional[list[int]]
    Mto_pago_min_mes_5: Optional[list[int]]
    Mto_pago_min_mes_6: Optional[list[int]]
    Mto_saldo_resumen_mes_1: Optional[list[int]]
    Mto_saldo_resumen_mes_2: Optional[list[int]]
    Mto_saldo_resumen_mes_3: Optional[list[int]]
    Mto_saldo_resumen_mes_4: Optional[list[int]]
    Mto_saldo_resumen_mes_5: Optional[list[int]]
    Mto_saldo_resumen_mes_6: Optional[list[int]]
    Pago_imputado_a_tc_mes_1: Optional[list[int]]
    Pago_imputado_a_tc_mes_2: Optional[list[int]]
    Pago_imputado_a_tc_mes_3: Optional[list[int]]
    Pago_imputado_a_tc_mes_4: Optional[list[int]]
    Pago_imputado_a_tc_mes_5: Optional[list[int]]
    Pago_imputado_a_tc_mes_6: Optional[list[int]]
    Tiene_plan_financiacion_ult_3m_gp: Optional[int]
    Tiene_plan_financiacion_ult_6m_gp: Optional[int]
    Tiene_plan_financiacion_ult_9m_gp: Optional[int]
    Tiene_plan_financiacion_ult_12m_gp: Optional[int]
    Tiene_debito_automatico_tarjeta_gp: Optional[int]
    Q_cuotas_restantes_total_gp: Optional[int]
    Dias_mora_tc: Optional[list[int]]
    Nivel_uso_tarjeta_1: Optional[list[int]]
    Nivel_uso_tarjeta_2: Optional[list[int]]
    Tiene_plan_financiacion_ult_6m: Optional[int]
    Tiene_plan_financiacion_ult_9m: Optional[int]

class Productos(BaseModel):
    Prestamos: Prestamos
    Cuenta_Sueldo: Cuenta_Sueldo
    Q_Productos_Vigentes: Optional[int]
    Q_Lineas_Producto_Vigentes: Optional[int]
    Q_Productos_Credito_GP: Optional[int]
    Caja_De_Ahorro: Caja_De_Ahorro
    Cuenta_Corriente: Cuenta_Corriente
    Plazo_Fijo: Plazo_Fijo
    Tarjetas: Tarjetas

# 3. Módulo de Gestión y Riesgos
# ----------------------------------------------------------------

class Solicitud(BaseModel):
    Canal_soli_producto: Optional[str]

class Home_Banking(BaseModel):
    Q_operaciones_digitales_mes: Optional[int]
    Es_usuario_hb: Optional[int]
    Q_operaciones_digitales_mes_gp: Optional[int]

class Canales_Y_Gestiones(BaseModel):
    Home_Banking: Home_Banking

class Ant_negativo(BaseModel):
    Mto_embargos_afip: Optional[int]
    Mto_embargos_soj_afip: Optional[int]
    Mto_embargos_bcra: Optional[int]
    Mto_embargos_arbe: Optional[int]
    Es_marca_cartera_vendida: Optional[int]
    Sem_indicador_banca: Optional[str]
    Es_dni_cuestionado: Optional[int]
    Es_cliente_factura_apocrifa: Optional[int]
    Es_baja_contable: Optional[int]
    Es_oficios_judiciales: Optional[int]
    Es_prestamo_reprogramado: Optional[int]
    Es_inhabilitado_cambios_bcra: Optional[int]
    Es_irrecuperable_cuenta_orden: Optional[int]
    Es_marca_legales: Optional[int]
    Es_estudio_cea: Optional[int]
    Mto_deuda_previsional_empleador_mes1: Optional[int]
    Mto_deuda_previsional_empleador_mes2: Optional[int]
    Mto_deuda_previsional_empleador_mes3: Optional[int]
    Mto_deuda_previsional_empleado: Optional[int]
    Periodo_deuda_previsional_empleado: Optional[str]

class Antecedentes_Negativos(BaseModel):
    Ant_negativo: Ant_negativo

class Morosidad(BaseModel):
    Mto_deuda_total_cliente: Optional[float]
    Mto_deuda_total_cliente_gp: Optional[int]
    Max_dias_mora_ult_mes: Optional[list[int]]
    Max_dias_mora_ult_3m: Optional[list[int]]
    Max_dias_mora_ult_6m: Optional[list[int]]
    Max_dias_mora_ult_9m: Optional[list[int]]
    Max_dias_mora_ult_12m: Optional[list[int]]
    Dias_mora: Optional[list[int]]
    Es_marca_reclasificado: Optional[int]
    Clasificacion_interna: Optional[int]
    Clasificacion_final: Optional[int]
    Mto_mora_gym: Optional[int]
    Fecha_envio_gym: Optional[str]

class Mora(BaseModel):
    Morosidad: Morosidad

class Riesgos(BaseModel):
    Antecedentes_Negativos: Antecedentes_Negativos
    Mora: Mora
    Id_corrida: Optional[str]
    Ult_fecha_eval_motor: Optional[str]
    Fecha_vencimiento_calif: Optional[str]
    Ult_fecha_calificacion_aprobada: Optional[str]
    Mto_pp_ult_calif: Optional[int]
    Fecha_mto_pp_ult_calif: Optional[str]
    Mto_visa_ultima_calif: Optional[int]
    Fecha_mto_visa_ult_calif: Optional[str]
    Mto_master_ult_calif: Optional[int]
    Fecha_mto_master_ult_calif: Optional[str]
    Mto_acuerdo_ult_calif: Optional[int]
    Fecha_mto_acuerdo_ult_calif: Optional[str]
    Mto_adelanto_haberes_ult_calif: Optional[int]
    Fecha_mto_adelanto_haberes_ult_calif: Optional[str]
    Mto_upgrade_master_ult_calif: Optional[int]
    Fecha_mto_upgrade_master_ult_calif: Optional[str]
    Mto_upgrade_visa_ult_calif: Optional[int]
    Fecha_mto_upgrade_visa_ult_calif: Optional[str]

# 4. Fillers y Modelos Finales
# ----------------------------------------------------------------

class Filler(BaseModel):
    Filler6: Optional[str]; Filler7: Optional[str]; Filler8: Optional[str]
    Filler9: Optional[str]; Filler10: Optional[str]; Filler11: Optional[str]
    Filler12: Optional[str]; Filler13: Optional[str]; Filler14: Optional[str]
    Filler15: Optional[str]; Filler16: Optional[str]; Filler17: Optional[str]
    Filler18: Optional[str]; Filler19: Optional[str]; Filler20: Optional[str]
    Date6: Optional[str]; Date7: Optional[str]; Date8: Optional[str]
    Date9: Optional[str]; Date10: Optional[str]; Date11: Optional[str]
    Date12: Optional[str]; Date13: Optional[str]; Date14: Optional[str]
    Date15: Optional[str]; Date16: Optional[str]; Date17: Optional[str]
    Date18: Optional[str]; Date19: Optional[str]; Date20: Optional[str]
    Decimal6: Optional[float] = 0; Decimal7: Optional[float] = 0
    Decimal8: Optional[float] = 0; Decimal9: Optional[float] = 0
    Decimal10: Optional[float] = 0; Decimal11: Optional[float] = 0
    Decimal12: Optional[float] = 0; Decimal13: Optional[float] = 0
    Decimal14: Optional[float] = 0; Decimal15: Optional[float] = 0
    Decimal16: Optional[float] = 0; Decimal17: Optional[float] = 0
    Decimal18: Optional[float] = 0; Decimal19: Optional[float] = 0
    Decimal20: Optional[float] = 0

class Campanas(BaseModel):
    Basesexternas: Basesexternas

class DatosImpositivos(BaseModel):
    Afip: AfipModel

class DatosPersonales(BaseModel):
    Aml: Aml
    Persona_humana: PersonaHumana

class Campanias(BaseModel):
    Campanas: Campanas

class Clientes(BaseModel):
    Datos_Impositivos: DatosImpositivos
    Datos_Personales: DatosPersonales
    Perfil_Tecnico: PerfilTecnico
    Tipo_proceso: Optional[str]

class InputModel(BaseModel):
    Clientes: Clientes
    Productos: Productos
    Solicitud: Solicitud
    Canales_Y_Gestiones: Canales_Y_Gestiones
    Riesgos: Riesgos
    Filler1: Optional[str]; Filler2: Optional[str]; Filler3: Optional[str]
    Filler4: Optional[str]; Filler5: Optional[str]
    Date1: Optional[str]; Date2: Optional[str]; Date3: Optional[str]
    Date4: Optional[str]; Date5: Optional[str]
    Decimal1: Optional[float]; Decimal2: Optional[float]; Decimal3: Optional[float]
    Decimal4: Optional[float]; Decimal5: Optional[float]
    Campanias: Campanias
    Filler: Filler
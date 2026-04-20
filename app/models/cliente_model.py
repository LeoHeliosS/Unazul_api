from datetime import date
from typing import Optional, List, Any

from pydantic import BaseModel, field_validator, ConfigDict


class InputModel(BaseModel):
    Clientes: Clientes
    Productos: Productos
    Solicitud: Solicitud
    Canales_Y_Gestiones: Canales_Y_Gestiones
    Riesgos: Riesgos
    Filler1:Optional[str]
    Filler2:Optional[str]
    Filler3:Optional[str]
    Filler4:Optional[str]
    Filler5:Optional[str]
    Date1:Optional[str]
    Date2:Optional[str]
    Date3:Optional[str]
    Date4:Optional[str]
    Date5: Optional[str]
    Decimal1: Optional[float]
    Decimal2: Optional[float]
    Decimal3: Optional[float]
    Decimal4: Optional[float]
    Decimal5: Optional[float]
    Campanias:Campanias
    Filler: Filler

#------------CLIENTE-------------------
class Clientes(BaseModel):
    Datos_Impositivos: DatosImpositivos
    Datos_Personales: DatosPersonales
    Perfil_Tecnico: PerfilTecnico
    Tipo_proceso: Optional[str] #null

class DatosImpositivos(BaseModel):
    Afip: AfipModel

class DatosPersonales(BaseModel):
    Aml: Aml
    Persona_humana: PersonaHumana

class PerfilTecnico(BaseModel):
    Acredita_haberes: Optional[AcreditaHaberes] #NO_VIENE_EN_EL_EJEMPLO!!!!!!!!!!
    Anses: Anses
    Bcra: Bcra
    Bcra_cr: Bcra_cr
    Cheques: Cheques
    Veraz:  Veraz
    Id_tipo_cliente: Optional[list[int]]
    Fecha_alta_cliente: Optional[str]
    Id_banco_cuenta: Optional[int]
    Id_segmento_comercial: Optional[int]# null,
    Id_cartera_comercial: Optional[int] #null,
    Id_sucursal_origen:Optional[int]
    Id_provincia:Optional[int]
    Score_nosis_empleador:Optional[int]
    Perfil:Perfil

class AfipModel (BaseModel):
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
    Es_sucesion: Optional[str]  # null,
    Categoria_autonomo: Optional[str]  # null,
    Actividad_monotributista: Optional[str]  # null

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
            return v.isoformat()  # Convierte 1979-11-27 (date) a "1979-11-27" (str)
        return v

class AcreditaHaberes(BaseModel):
    Mto_haber_acreditado:Optional[List[float]]
    Mto_haber_acreditado_mes_1:Optional[List[float]]
    Mto_haber_acreditado_mes_2:Optional[List[float]]
    Mto_haber_acreditado_mes_3:Optional[List[float]] #null
    Mto_prom_haberes_acreditados_trim:Optional[float]
    Acredita_haberes:Optional[int]
    Cuit_empleador:Optional[List[str]] #Lista de que tipo??
    Id_actividad_empleado:Optional[str]
    Id_sector_empleador:Optional[str] #null
    Mto_prom_haberes_acreditados_trim_gp:Optional[int]
    Mto_haber_acreditado_gp:Optional[int]
    Fecha_ult_hab_acreditado:Optional[List[str]] #Lista de que tipo??
    Id_convenio:Optional[List[int]]
    Rel_ingreso_mensual_imvym:Optional[int]

class Anses(BaseModel):
    Nro_beneficio_anses:Optional[List[int]] #Lista de que tipo??
    Mto_beneficio_anses:Optional[List[float]] #Lista de que tipo??

class Bcra(BaseModel):
    Q_entidades_gr1:Optional[int]
    Q_entidades_gr2:Optional[int]
    Q_entidades_gr3:Optional[int]
    Q_entidades_gr4:Optional[int]
    Q_entidades_deuda:Optional[int]
    Q_entidades_sit_mayor_a_1:Optional[int]
    Max_sit:Optional[int]
    Max_sit_3m:Optional[int]
    Max_sit_6m:Optional[int]
    Max_sit_9m:Optional[int]
    Max_sit_12m:Optional[int]
    Por_deuda_bcos_gr1:Optional[int]
    Por_deuda_bcos_gr2:Optional[int]
    Por_deuda_bcos_gr3:Optional[int]
    Por_deuda_bcos_gr4:Optional[int]
    Mto_deuda_sit_mayor_a_1:Optional[int]
    Mto_deuda_sit_mayor_a_1_3m:Optional[int]
    Mto_deuda_sit_mayor_a_1_6m:Optional[int]
    Mto_deuda_sit_mayor_a_1_9m:Optional[int]
    Mto_deuda_sit_mayor_a_1_12m:Optional[int]
    Mto_deuda_total:Optional[int]
    Mto_deuda_total_2m:Optional[int]
    Mto_deuda_total_3m:Optional[int]
    Mto_deuda_total_6m:Optional[int]
    Mto_deuda_total_9m:Optional[int]
    Mto_deuda_total_12m:Optional[int]
    Mto_deuda_total_gp:Optional[int]
    Mto_deuda_total_gp_3m:Optional[int]
    Mto_deuda_total_gp_6m:Optional[int]
    Mto_deuda_total_gp_9m:Optional[int]
    Mto_deuda_total_gp_12m:Optional[int]
    Es_marca_endeudamiento:Optional[int]
    Id_entidades_deuda: Optional[List[int]] #Lista de que tipo??
    Sit_deuda_entidades: Optional[List[int]] #Lista de que tipo??
    Mto_deuda_entidades: Optional[List[float]]
    Es_marca_moroso_ex: Optional[int]

class Bcra_cr(BaseModel):
    Mto_cheq_rech_vicios_formales:Optional[int]
    Q_cheq_rech_vicios_formales:Optional[int]
    Q_cheq_rech_sf_pagos:Optional[int]
    Mto_cheq_rech_sf_pagos:Optional[int]
    Q_cheq_rech_sf_impagos:Optional[int]
    Q_cheq_rech_sf_impagos_6m:Optional[int]
    Q_cheq_rech_sf_impagos_9m:Optional[int]
    Q_cheq_rech_sf_impagos_12m:Optional[int]
    Mto_cheq_rech_sf_impagos:Optional[int]
    Mto_cheq_rech_sf_impagos_6m:Optional[int]
    Mto_cheq_rech_sf_impagos_9m:Optional[int]
    Mto_cheq_rech_sf_impagos_12m:Optional[int]

class Cheques(BaseModel):
    Q_cheq_rech_bco_vicios_formales:Optional[int]
    Mto_cheq_rech_bco_vicios_formales:Optional[int]
    Q_cheq_rech_bco_sf_impagos:Optional[int]
    Q_cheq_rech_bco_sf_impagos_6m:Optional[int]
    Q_cheq_rech_bco_sf_impagos_12m:Optional[int]
    Q_cheq_rech_bco_sf_impagos_24m:Optional[int]
    Mto_cheq_rech_bco_sf_impagos:Optional[int]
    Mto_cheq_rech_bco_sf_impagos_6m:Optional[int]
    Mto_cheq_rech_bco_sf_impagos_12m:Optional[int]
    Mto_cheq_rech_bco_sf_impagos_24m:Optional[int]
    Q_cheq_rech_bco_sf_pagos:Optional[int]
    Q_cheq_rech_bco_sf_pagos_6m:Optional[int]
    Q_cheq_rech_bco_sf_pagos_12m:Optional[int]
    Q_cheq_rech_bco_sf_pagos_24m:Optional[int]
    Mto_cheq_rech_bco_sf_pagos:Optional[int]
    Mto_cheq_rech_bco_sf_pagos_6m:Optional[int]
    Mto_cheq_rech_bco_sf_pagos_12m:Optional[int]
    Mto_cheq_rech_bco_sf_pagos_24m:Optional[int]

class Veraz(BaseModel):
    Vz_nro_cuil:Optional[int] #null,
    Vz_dto_validado:Optional[int]
    Vz_score_riesgo:Optional[int]
    Vz_score_poblacion:Optional[int] #null,
    Vz_geonse:Optional[int] #null,
    Vz_edad:Optional[int]
    Vz_sexo:Optional[int] #null,
    Vz_nombre_apellido:Optional[int] #null,
    Vz_validacion_identidad:Optional[int] #null,
    Vz_obra_social_titular:Optional[int] #null,
    Vz_cat_monotributo:Optional[int] #null,
    Vz_actividad_autonomos:Optional[int] #null,
    Vz_marca_actividad:Optional[int]
    Vz_income_predictor:Optional[int] #null
    Vz_cp:Optional[int] #null
    Vz_q_productos_sit_2_bcra:Optional[int]
    Vz_q_productos_sit_2_bcra_ult_60m:Optional[int]
    Vz_q_meses_desde_ult_sit_mayor_igual_2:Optional[int]
    Vz_q_antiguedad_meses_tc_activa:Optional[int]
    Vz_q_prestamos_activos:Optional[int]
    Vz_max_saldo_mto_pp_ult_3m:Optional[int]
    Vz_q_cons_dist_ent_ult_12m:Optional[int]
    Vz_q_meses_ult_cons_financiera:Optional[int]
    Vz_q_meses_ult_cons_tec:Optional[int]
    Vz_q_cons_fin_ult_6m:Optional[int]
    Vz_actividad_empleador:Optional[int] #null
    Vz_q_meses_desde_ult_sit_2:Optional[int]
    Vz_max_limite_tc:Optional[int]
    Vz_grupo_bco_max_limite_tc:Optional[int] #null
    Vz_compromiso_pp_tc:Optional[int]
    Vz_cap_activ_autonomos:Optional[int] #null,
    Vz_cons_ult_6m:Optional[int]
    Vz_cap_activ_empleador:Optional[int] #null
    Vz_prod_sit_bcra_mayor_a_1_ult_60m:Optional[int]
    Vz_pre_saldos_total_activas_ult_3m:Optional[int]
    Vz_suma_lim_compra_tc_ult_6m:Optional[int]
    Vz_tarjeta_saldo_suma:Optional[int]
    Vz_bureau_tarjetas_saldo_maximo_ult_12m:Optional[int]
    Vz_fecha_actualizacion:Optional[str]
    Vz_ult_modelo_actualizado:Optional[int] #null

class Perfil(BaseModel):
    Id_tipo_cliente_mes_1: Optional[list[int]] #sin datos de la lista
    Id_tipo_cliente_mes_2: Optional[list[int]] #sin datos de la lista
    Id_tipo_cliente_mes_3: Optional[list[int]] #sin datos de la lista
    Es_socio: Optional[int]
    Es_socio_mto_presunto: Optional[int]
    Es_socio_segmento_ccial: Optional[int]#null

#------------PRODUCTOS-------------------

class Productos(BaseModel):
    Prestamos: Prestamos
    Cuenta_Sueldo: Cuenta_Sueldo
    Q_Productos_Vigentes:Optional[int]
    Q_Lineas_Producto_Vigentes: Optional[int]
    Q_Productos_Credito_GP: Optional[int]
    Caja_De_Ahorro:Caja_De_Ahorro
    Cuenta_Corriente:Cuenta_Corriente
    Plazo_Fijo:Plazo_Fijo
    Tarjetas:Tarjetas

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

class Adelanto_haberes(BaseModel):
    Mto_adelanto_haberes: Optional[int]

class Compra_De_Cartera(BaseModel):
    Es_pp_vigente_ccart: Optional[int]
    Capital_origen_ccart: Optional[int]
    Fecha_alta_ccart_vigente: Optional[str] #null
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
    Es_pp_vigente_refi:Optional[int]
    Capital_Origen_Refi:Optional[int]
    Fecha_alta_refi_vigente:Optional[str]
    Mto_deuda_refi_vigente:Optional[int]
    Nro_cuota_refi_vigente:Optional[int]
    Q_cuotas_total_refi:Optional[int]
    Q_cuotas_pagas_refi:Optional[int]
    Mto_cuota_vigente_refi:Optional[int]

class Reprogramados(BaseModel):
    Capital_origen_repro:Optional[int]
    Fecha_alta_repro_vigente:Optional[str]
    Mto_deuda_repro_vigente:Optional[int]
    Q_cuotas_repro_vigentes:Optional[int]
    Mto_cuota_repro_vigente:Optional[int]
    Mto_deuda_repro_exigible:Optional[int]
    Mto_cuota_repro_exigible:Optional[int]

class Cuenta_Sueldo(BaseModel):
    Nro_cuenta_sueldo: Optional[int]
    Fecha_alta_cuenta_sueldo: Optional[str]
    Es_cuenta_sueldo: Optional[int]
    Tipo_cuenta_sueldo: Optional[int] #null
    Producto_cuenta_sueldo: Optional[str] #null

class Caja_De_Ahorro(BaseModel):
    Es_ca_activo:Optional[int]
    Saldo_ca_mes_1:Optional[int]
    Saldo_ca_mes_2:Optional[int]
    Saldo_ca_mes_3:Optional[int]

class Cuenta_Corriente (BaseModel):
    Es_cc_activo:Optional[int]
    Mto_saldo_acuerdo_cc:Optional[int]
    Mto_acuerdo_cc:Optional[int]
    Fecha_alta_acuerdo_cc:Optional[str]
    Saldo_cc_mes_1:Optional[int]
    Saldo_cc_mes_2:Optional[int]
    Saldo_cc_mes_3:Optional[int]

class Plazo_Fijo(BaseModel):
    Es_pf_activo:Optional[int]
    Monto_pf_mes_1:Optional[int]
    Monto_pf_mes_2:Optional[int]
    Monto_pf_mes_3:Optional[int]
    Monto_pf_mes_4:Optional[int]
    Monto_pf_mes_5:Optional[int]
    Monto_pf_mes_6:Optional[int]

class Tarjetas(BaseModel):
    Fecha_aumento_limite_transitorio:Optional[str]
    Nro_cuenta_tc:Optional[list[int]]
    Nro_sucursal_cuenta_tc:Optional[list[int]]
    Tipo_plastico_tc:Optional[list[int]]
    Marca_tc:Optional[list[int]]
    Mto_limite_compras_cuotas: Optional[int]#Optional[list[int]]
    Mto_saldo_deuda_total:Optional[int]
    Mto_abonado:Optional[list[int]]
    Es_pago_minimo:Optional[list[int]]
    Nivel_uso_tarjeta:Optional[list[int]]
    Fecha_alta_tc:Optional[list[str]]
    Fecha_aumento_limite_compra:Optional[str]
    Mto_limite_compra:Optional[list[int]]
    Tiene_plan_financiacion:Optional[int]
    Tiene_plan_financiacion_ult_12m:Optional[int]
    Tiene_plan_financiacion_ult_3m:Optional[int]
    Mto_limite_compra_gp:Optional[int]
    Mto_saldo_deuda_total_gp:Optional[int]
    Nivel_uso_tarjetas_gp:Optional[int]
    Min_nivel_uso_tarjeta_trim_gp:Optional[int]
    Max_nivel_uso_tarjeta_trim_gp:Optional[int]
    Prom_nivel_uso_tarjeta_trim_gp:Optional[int]
    Evolucion_nivel_uso_tarjeta_gp:Optional[int]
    Nivel_pago_tarjeta_gp:Optional[int]
    Mto_pago_min_mes_1:Optional[list[int]]
    Mto_pago_min_mes_2:Optional[list[int]]
    Mto_pago_min_mes_3:Optional[list[int]]
    Mto_pago_min_mes_4:Optional[list[int]]
    Mto_pago_min_mes_5:Optional[list[int]]
    Mto_pago_min_mes_6:Optional[list[int]]
    Mto_saldo_resumen_mes_1:Optional[list[int]]
    Mto_saldo_resumen_mes_2:Optional[list[int]]
    Mto_saldo_resumen_mes_3:Optional[list[int]]
    Mto_saldo_resumen_mes_4:Optional[list[int]]
    Mto_saldo_resumen_mes_5:Optional[list[int]]
    Mto_saldo_resumen_mes_6:Optional[list[int]]
    Pago_imputado_a_tc_mes_1:Optional[list[int]]
    Pago_imputado_a_tc_mes_2:Optional[list[int]]
    Pago_imputado_a_tc_mes_3:Optional[list[int]]
    Pago_imputado_a_tc_mes_4:Optional[list[int]]
    Pago_imputado_a_tc_mes_5:Optional[list[int]]
    Pago_imputado_a_tc_mes_6:Optional[list[int]]
    Tiene_plan_financiacion_ult_3m_gp:Optional[int]
    Tiene_plan_financiacion_ult_6m_gp:Optional[int]
    Tiene_plan_financiacion_ult_9m_gp:Optional[int]
    Tiene_plan_financiacion_ult_12m_gp:Optional[int]
    Tiene_debito_automatico_tarjeta_gp:Optional[int]
    Q_cuotas_restantes_total_gp:Optional[int]
    Dias_mora_tc:Optional[list[int]]
    Nivel_uso_tarjeta_1:Optional[list[int]]
    Nivel_uso_tarjeta_2:Optional[list[int]]
    Tiene_plan_financiacion_ult_6m:Optional[int]
    Tiene_plan_financiacion_ult_9m:Optional[int]

#-----------------SOLICITUD------------------------------------

class Solicitud(BaseModel):
    Canal_soli_producto: Optional[str]

# ----------------CANALES Y GESTIONES--------------------------

class Canales_Y_Gestiones(BaseModel):
    Home_Banking: Home_Banking

class Home_Banking(BaseModel):
    Q_operaciones_digitales_mes:Optional[int]
    Es_usuario_hb:Optional[int]
    Q_operaciones_digitales_mes_gp:Optional[int]

#-----------------RIESGOS--------------------------------------

class Riesgos(BaseModel):
    Antecedentes_Negativos: Antecedentes_Negativos
    Mora: Mora
    Id_corrida:Optional[str]
    Ult_fecha_eval_motor:Optional[str]
    Fecha_vencimiento_calif:Optional[str]
    Ult_fecha_calificacion_aprobada:Optional[str]
    Mto_pp_ult_calif:Optional[int]
    Fecha_mto_pp_ult_calif:Optional[str]
    Mto_visa_ultima_calif:Optional[int]
    Fecha_mto_visa_ult_calif:Optional[str]
    Mto_master_ult_calif:Optional[int]
    Fecha_mto_master_ult_calif:Optional[str]
    Mto_acuerdo_ult_calif:Optional[int]
    Fecha_mto_acuerdo_ult_calif:Optional[str]
    Mto_adelanto_haberes_ult_calif:Optional[int]
    Fecha_mto_adelanto_haberes_ult_calif:Optional[str]
    Mto_upgrade_master_ult_calif:Optional[int]
    Fecha_mto_upgrade_master_ult_calif:Optional[str]
    Mto_upgrade_visa_ult_calif:Optional[int]
    Fecha_mto_upgrade_visa_ult_calif:Optional[str]

class Antecedentes_Negativos(BaseModel):
    Ant_negativo: Ant_negativo

class Ant_negativo(BaseModel):
    Mto_embargos_afip:Optional[int]
    Mto_embargos_soj_afip:Optional[int]
    Mto_embargos_bcra:Optional[int]
    Mto_embargos_arbe:Optional[int]
    Es_marca_cartera_vendida:Optional[int]
    Sem_indicador_banca:Optional[int]
    Es_dni_cuestionado:Optional[int]
    Es_cliente_factura_apocrifa:Optional[int]
    Es_baja_contable:Optional[int]
    Es_oficios_judiciales:Optional[int]
    Es_prestamo_reprogramado:Optional[int]
    Es_inhabilitado_cambios_bcra:Optional[int]
    Es_irrecuperable_cuenta_orden:Optional[int]
    Es_marca_legales:Optional[int]
    Es_estudio_cea:Optional[int]
    Mto_deuda_previsional_empleador_mes1:Optional[int]
    Mto_deuda_previsional_empleador_mes2:Optional[int]
    Mto_deuda_previsional_empleador_mes3:Optional[int]
    Mto_deuda_previsional_empleado:Optional[int]
    Periodo_deuda_previsional_empleado:Optional[str] #null

class Mora(BaseModel):
    Morosidad: Morosidad

class Morosidad(BaseModel):
    Mto_deuda_total_cliente:Optional[int]
    Mto_deuda_total_cliente_gp:Optional[int]
    Max_dias_mora_ult_mes:Optional[list[int]]
    Max_dias_mora_ult_3m:Optional[list[int]]
    Max_dias_mora_ult_6m:Optional[list[int]]
    Max_dias_mora_ult_9m:Optional[list[int]]
    Max_dias_mora_ult_12m:Optional[list[int]]
    Dias_mora:Optional[list[int]]
    Es_marca_reclasificado:Optional[int]
    Clasificacion_interna:Optional[int]
    Clasificacion_final:Optional[int]
    Mto_mora_gym:Optional[int]
    Fecha_envio_gym:Optional[str]

#-----------------CAMPANIAS--------------------------------------

class Campanias(BaseModel):
    Campanas:Campanas

class Campanas(BaseModel):
    Basesexternas: Basesexternas

class Basesexternas(BaseModel):
    Politica_riesgo: Optional[int] #null
    Segmento_riesgos: Optional[int] #null,
    Mto_haber_informado_empleador: Optional[int]
    Ponderador: Optional[int]
    Codigo_limite_visa: Optional[int] #null,
    Cuit_informado_empleador: Optional[int] #null,
    Nombre_informado_empleador: Optional[str] #null,
    Banco_calificador: Optional[str] #null,
    Politica_credito: Optional[str] #null,
    Descripcion_base: Optional[str] #null

#-----------------FILLERS--------------------------------------

class Filler(BaseModel):
    Filler6:Optional[str] #null,
    Filler7:Optional[str] #null,
    Filler8:Optional[str] #null,
    Filler9:Optional[str] #null,
    Filler10:Optional[str] #null,
    Filler11:Optional[str] #null,
    Filler12:Optional[str] #null,
    Filler13:Optional[str] #null,
    Filler14:Optional[str] #null,
    Filler15:Optional[str] #null,
    Filler16:Optional[str] #null,
    Filler17:Optional[str] #null,
    Filler18:Optional[str] #null,
    Filler19:Optional[str] #null,
    Filler20:Optional[str] #null,
    Date6: Optional[str] #null,
    Date7: Optional[str] #null,
    Date8: Optional[str] #null,
    Date9: Optional[str] #null,
    Date10: Optional[str] #null,
    Date11: Optional[str] #null,
    Date12: Optional[str] #null,
    Date13: Optional[str] #null,
    Date14: Optional[str] #null,
    Date15: Optional[str] #null,
    Date16: Optional[str] #null,
    Date17: Optional[str] #null,
    Date18: Optional[str] #null,
    Date19: Optional[str] #null,
    Date20: Optional[str] #null,
    Decimal6:Optional[float]# 0,
    Decimal7:Optional[float]# 0,
    Decimal8:Optional[float]# 0,
    Decimal9:Optional[float]# 0,
    Decimal10:Optional[float]# 0,
    Decimal11:Optional[float]# 0,
    Decimal12:Optional[float]# 0,
    Decimal13:Optional[float]# 0,
    Decimal14:Optional[float]# 0,
    Decimal15:Optional[float]# 0,
    Decimal16:Optional[float]# 0,
    Decimal17:Optional[float]# 0,
    Decimal18:Optional[float]# 0,
    Decimal19:Optional[float]# 0,
    Decimal20:Optional[float]# 0

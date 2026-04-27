from datetime import date
from typing import get_args, get_origin, Union, List
from pydantic import BaseModel

def patch_json(original, update):
    for key, value in update.items():
        if key in original:
            if isinstance(value, dict) and isinstance(original[key], dict):
                patch_json(original[key], value)
            elif value is not None and value != [] and original[key] is None :
                print('Campo pisado', key )
                original[key] = value
#        else:
 #           if value is not None:
  #              original[key] = value
    return original


def clean_nones_with_model(data: dict, model_class: type[BaseModel]) -> dict:

    cleaned_data = {}

    for field_name, field_info in model_class.model_fields.items():
        value = data.get(field_name)

        annotation = field_info.annotation
        origin = get_origin(annotation)
        args = get_args(annotation)

        if origin is Union:
            actual_type = next((arg for arg in args if arg is not type(None)), any)
        else:
            actual_type = annotation

        if isinstance(actual_type, type) and issubclass(actual_type, BaseModel):
            sub_dict = value if isinstance(value, dict) else {}
            cleaned_data[field_name] = clean_nones_with_model(sub_dict, actual_type)

        elif value is None:
            especificos = {
                "Id_convenio": [0, 0, 0],
                "Tipo_plastico_tc": [0, 0, 0, 0, 0],
                "Mto_limite_compra": [0, 0, 0, 0, 0],
                "Max_dias_mora_ult_mes": [0, 0, 0, 0],
                "Dias_mora": [0, 0, 0, 0],
                "Fecha_alta_ccart_vigente": None,
                "Fecha_alta_lh_vigente": None,
                "Fecha_alta_refi_vigente": None,
                "Fecha_alta_repro_vigente": None,
                "Fecha_nacimiento": None,
                "Fecha_alta_cliente": None,
                "Vz_fec_act_mod_1": None,
                "Vz_fec_act_mod_2": None,
                "Vz_fec_act_mod_3": None,
                "Fecha_alta_cuenta_sueldo": None,
                "Fecha_alta_acuerdo_cc": None,
                "Fecha_aumento_limite_transitorio": None,
                "Fecha_aumento_limite_compra": None,
                "Date1": None,
                "Date2": None,
                "Date3": None,
                "Date4": None,
                "Date5": None,
                "Fecha_ult_proceso_calif": None,
                'Fecha_alta_cliente':'19000101',
                'Vz_fecha_actualizacion':'19000101'

            }

            if field_name in especificos:
                cleaned_data[field_name] = especificos[field_name]
            elif get_origin(actual_type) is list or "List" in str(actual_type):
                cleaned_data[field_name] = [0]
            elif actual_type is int or actual_type is float:
                cleaned_data[field_name] = 0
            elif actual_type is str:
                cleaned_data[field_name] = ""
            else:
                cleaned_data[field_name] = 0
        else:
            cleaned_data[field_name] = value

    return cleaned_data
from app.models.AuditoriaModel import AuditoriaModel
from app.models.ResultadoModel import ResultadoModel
from app.models.cliente_model import InputModel
from typing import Optional, List
from pydantic import BaseModel, field_validator


class ExperianJsonModel(BaseModel):
    DAJSONDocumentV2:DAJSONDocumentV2Model

class DAJSONDocumentV2Model(BaseModel):
    OCONTROL: OcontrolModel
    Auditoria: AuditoriaModel
    Input: InputModel
    Resultado: ResultadoModel

class OcontrolModel(BaseModel):
    ALIAS: Optional[str]
    SIGNATURE: Optional[str]
    DALOGLEVEL: Optional[int]
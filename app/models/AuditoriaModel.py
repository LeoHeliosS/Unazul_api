from app.models.cliente_model import InputModel
from typing import Optional, List

from pydantic import BaseModel, field_validator


class DeriveddataModel(BaseModel):
    Outcome_id: Optional[str] = None
    Outcome_name: Optional[str] = None
    Deriveddatascript_id: Optional[str] = None
    Deriveddatascript_name: Optional[str] = None
    Testgroup_id: Optional[str] = None
    Testgroup_name: Optional[str] = None
    Leafnode_id: Optional[str] = None
    Leafnode_name: Optional[str] = None

class ClassSetModel(BaseModel):
    ClassSetId: Optional[str] = None
    ClassSetName: Optional[str] = None
    IntervalId: Optional[str] = None
    IntervalName: Optional[str] = None

class IndexDetailModel(BaseModel):
    Leafnode_id: Optional[str] = None
    Leafnode_name: Optional[str] = None
    Outcome_id: Optional[str] = None
    Outcome_name: Optional[str] = None
    Indextable_id: Optional[str] = None
    Indextable_name: Optional[str] = None
    Testgroupset_id: Optional[str] = None
    Testgroupset_name: Optional[str] = None

class ProcesoModel(BaseModel):
    Leafnode_id: Optional[str] = None
    Leafnode_name: Optional[str] = None
    Outcome_id: Optional[str] = None
    Outcome_name: Optional[str] = None
    Testgroupset_id: Optional[str] = None
    Testgroupset_name: Optional[str] = None
    Decisionprocess_tree_id: Optional[str] = None
    Decisionprocess_tree_name: Optional[str] = None

class ScoringModel(BaseModel):
    Leafnode_id: Optional[str] = None
    Leafnode_name: Optional[str] = None
    Outcome_id: Optional[str] = None
    Outcome_name: Optional[str] = None
    Scorecard_id: Optional[str] = None
    Scorecard_name: Optional[str] = None
    Testgroupset_id: Optional[str] = None
    Testgroupset_name: Optional[str] = None

class TreatmentTableModel(BaseModel):
    Leafnode_id: Optional[str] = None
    Leafnode_name: Optional[str] = None
    Outcome_id: Optional[str] = None
    Outcome_name: Optional[str] = None
    Treatmenttable_id: Optional[str] = None
    Treatmenttable_name: Optional[str] = None
    Treatment_id: Optional[str] = None
    Treatment_name: Optional[str] = None
    Testgroupset_id: Optional[str] = None
    Testgroupset_name: Optional[str] = None

class BooleanExpressionModel(BaseModel):
    BooleanExpresionId: Optional[str] = None
    BoooleanExpressionName: Optional[str] = None #REVISAR!!!!!
    OutcomeId: Optional[str] = None
    OutcomeName: Optional[str] = None

class BancoModel(BaseModel):
    ClassSet: Optional[ClassSetModel] = None

class IndexacionDeDatosModel(BaseModel):
    Index1: Optional[IndexDetailModel] = None
    Index2: Optional[IndexDetailModel] = None
    Index3: Optional[IndexDetailModel] = None
    Index4: Optional[IndexDetailModel] = None
    Index5: Optional[IndexDetailModel] = None
    Proceso: Optional[ProcesoModel] = None

class ScorePreburoModel(BaseModel):
    Scoring: Optional[ScoringModel] = None
    Proceso: Optional[ProcesoModel] = None
    Deriveddata: Optional[DeriveddataModel] = None

class PoliticasFiltrosModel(BaseModel):
    Learnode_id: Optional[str] = None  #REVISAR!!!!!
    Leafnode_name: Optional[str] = None
    Outcome_id: Optional[str] = None
    Otucome_name: Optional[str] = None #REVISAR!!!!!
    Testgroupset_id: Optional[str] = None
    Testgroupset_name: Optional[str] = None

class FiltrosDurosModel(BaseModel):
    Politicas: Optional[PoliticasFiltrosModel] = None

class CalculosInicialesModel(BaseModel):
    Deriveddata: Optional[DeriveddataModel] = None

class LlamarServicio2Model(BaseModel):
    BooleanExpresionId: Optional[str] = None
    BoooleanExpressionName: Optional[str] = None #REVISAR!!!!!
    OutcomeId: Optional[str] = None
    OutcomeName: Optional[str] = None
    BooleanExpresion: Optional[BooleanExpressionModel] = None

class LlamarABureauModel(BaseModel):
    TreatmentTable: Optional[TreatmentTableModel] = None

class CalculosFinalesModel(BaseModel):
    Deriveddata: Optional[DeriveddataModel] = None

class TransformacionDeDatosModel(DeriveddataModel): pass
class CalculosIntermediosModel(DeriveddataModel): pass

class LlamarAEvaluacionModel(BaseModel):
    BooleanExpresionId: Optional[str] = None
    BoooleanExpressionName: Optional[str] = None #REVISAR!!!!!
    OutcomeId: Optional[str] = None
    OutcomeName: Optional[str] = None

class ScoreDeOriginacionModel(BaseModel):
    Scoring: Optional[ScoringModel] = None
    Proceso: Optional[ProcesoModel] = None
    Deriveddata: Optional[DeriveddataModel] = None

class IngresoInferidoModel(BaseModel):
    Proceso: Optional[ProcesoModel] = None
    Deriveddata: Optional[DeriveddataModel] = None
    TreatmentTable: Optional[TreatmentTableModel] = None

class PreburoModel(BaseModel):
    CalculosIniciales: Optional[CalculosInicialesModel] = None
    LlamarServicio2: Optional[LlamarServicio2Model] = None
    Banco: Optional[BancoModel] = None
    IndexacionDeDatos: Optional[IndexacionDeDatosModel] = None
    ScorePreburo: Optional[ScorePreburoModel] = None
    FiltrosDuros: Optional[FiltrosDurosModel] = None
    LlamarABureau: Optional[LlamarABureauModel] = None
    CalculosFinales: Optional[CalculosFinalesModel] = None
    TransformacionDeDatos: Optional[TransformacionDeDatosModel] = None
    CalculosIntermedios: Optional[CalculosIntermediosModel] = None
    LlamarAEvaluacion: Optional[LlamarAEvaluacionModel] = None

class EvaluacionModel(BaseModel):
    CalculosIniciales: Optional[CalculosInicialesModel] = None
    LlamarServicio2: Optional[LlamarServicio2Model] = None
    Banco: Optional[BancoModel] = None
    IndexacionDeDatos: Optional[IndexacionDeDatosModel] = None
    ScoreDeOriginacion: Optional[ScoreDeOriginacionModel] = None
    NivelDeRiesgo: Optional[LlamarABureauModel] = None
    ClasificacionCliente: Optional[LlamarABureauModel] = None
    CapacidadDePago: Optional[LlamarABureauModel] = None
    ExposicionMensual: Optional[LlamarABureauModel] = None
    ExposicionGlobal: Optional[LlamarABureauModel] = None
    CondicionDelPrestamos: Optional[LlamarABureauModel] = None
    CondicionTc: Optional[LlamarABureauModel] = None
    Documentacion: Optional[LlamarABureauModel] = None
    Verificacion: Optional[LlamarABureauModel] = None
    NivelDeFirma: Optional[LlamarABureauModel] = None
    IngresoInferido: Optional[IngresoInferidoModel] = None
    Endeudamiento: Optional[CalculosFinalesModel] = None
    Politicas: Optional[FiltrosDurosModel] = None
    CalculosFinales: Optional[CalculosFinalesModel] = None
    TransformacionDeDatos: Optional[TransformacionDeDatosModel] = None
    CalculosIntermedios: Optional[CalculosIntermediosModel] = None

class AuditoriaModel(BaseModel):
    Preburo: Optional[PreburoModel] = None
    Evaluacion: Optional[EvaluacionModel] = None

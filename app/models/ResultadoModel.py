from typing import Optional, List, Any
from pydantic import BaseModel


class FillerModel(BaseModel):
    Filler1n6: Optional[str] = None
    Filler2n6: Optional[str] = None
    Filler3n15: Optional[str] = None
    Filler4n15: Optional[str] = None
    Filler5x20: Optional[str] = None
    Filler6x20: Optional[str] = None
    Randomnumber1: Optional[str] = None
    Randomnumber2: Optional[str] = None
    Randomnumber3: Optional[str] = None

class VarNumTextModel(BaseModel):
    Varnum: Optional[str] = None
    Vartext: Optional[str] = None

class VarNumTextExtendedModel(BaseModel):
    Varnum1: Optional[str] = None
    Varnum2: Optional[str] = None
    Varnum3: Optional[str] = None
    Varnum4: Optional[str] = None
    Varnum5: Optional[str] = None
    Vartext1: Optional[str] = None
    Vartext2: Optional[str] = None
    Vartext3: Optional[str] = None
    Vartext4: Optional[str] = None
    Vartext5: Optional[str] = None

class ScoringResultModel(BaseModel):
    Score: Optional[str] = None
    Scorename: Optional[str] = None
    Reasoncode: List[Any] = []
    Index: Optional[str] = None
    Scorefinal: Optional[str] = None
    Tabla: List[Any] = []

class PoliticasResultModel(BaseModel):
    Text: Optional[str] = None
    DecisionCategory: Optional[str] = None
    ReasonCodeTable: List[Any] = []
    SortedReasonCodeTable: List[Any] = []

class DescripcionCodigoModel(BaseModel):
    Descripcion: Optional[str] = None
    Codigo: Optional[str] = None


class PrebureauResultModel(BaseModel):
    Cf: Optional[FillerModel] = None
    Ci: Optional[FillerModel] = None
    IndexacionDeDatos: Optional[Any] = None # Contiene SubRutina
    Score: Optional[Any] = None # Contiene Scoring y Deriveddata
    FiltrosDuros: Optional[Any] = None # Contiene Politicas
    LlamarABuro: Optional[Any] = None

class PrebureauSubRutina(BaseModel):
    SubRutina: Optional[VarNumTextExtendedModel] = None

class PrebureauScore(BaseModel):
    Scoring: Optional[ScoringResultModel] = None
    Deriveddata: Optional[VarNumTextModel] = None

class PrebureauFiltros(BaseModel):
    Politicas: Optional[PoliticasResultModel] = None

class LlamarABuroModel(BaseModel):
    Llamar: Optional[str] = None
    Bureau1: Optional[str] = None
    Bureau2: Optional[str] = None
    Bureau3: Optional[str] = None
    Bureau4: Optional[str] = None
    Codbureau1: Optional[str] = None
    Codbureau2: Optional[str] = None
    Codbureau3: Optional[str] = None
    Codbureau4: Optional[str] = None
    Oblbureau1: Optional[str] = None
    Oblbureau2: Optional[str] = None
    Oblbureau3: Optional[str] = None
    Oblbureau4: Optional[str] = None
    Validezbureau1: Optional[str] = None
    Validezbureau2: Optional[str] = None
    Validezbureau3: Optional[str] = None
    Validezbureau4: Optional[str] = None

class IngresoInferidoProcessModel(BaseModel):
    Varnum: Optional[str] = None
    Vartext: Optional[str] = None
    Ingresoinferido: Optional[str] = None
    Fuenteingresoelegida: Optional[str] = None
    Mto_ingreso: Optional[str] = None

class EndeudamientoModel(BaseModel):
    Endeudamientomensual: Optional[str] = None
    Endeudamientoglobal: Optional[str] = None
    Pagominimotc_cta1: Optional[str] = None
    Ctaprestamosinternos_cta1: Optional[str] = None
    Adelantodesueldo_cta1: Optional[str] = None
    Acuerdoctacte_cta1: Optional[str] = None
    Otrosgastos_cta1: Optional[str] = None
    Compromisosf_cta1: Optional[str] = None
    Ctaprestamosinternos_cta2: Optional[str] = None
    Adelantodesueldo_cta2: Optional[str] = None
    Acuerdoctacte_cta2: Optional[str] = None
    Otrosgastos_cta2: Optional[str] = None
    Compromisosf_cta2: Optional[str] = None
    Pagominimotc_cta2: Optional[str] = None

class ExposicionMensualModel(BaseModel):
    Couta: Optional[str] = None
    Cuota1: Optional[str] = None
    Cuota2: Optional[str] = None
    Cuotamaximactacte: Optional[str] = None
    Cuotamaximatc: Optional[str] = None
    Cuotamaximaah: Optional[str] = None

class ExposicionGlobalModel(BaseModel):
    Monto1: Optional[str] = None
    Monto2: Optional[str] = None
    Montomaximoctacte: Optional[str] = None
    Montomaximotc: Optional[str] = None
    Montomaximoah: Optional[str] = None
    Monto: Optional[str] = None

class CondicionPrestamosModel(BaseModel):
    Bonificagastos: Optional[str] = None
    Cargossaldos: Optional[str] = None
    Plazomax: Optional[str] = None
    Plazomin: Optional[str] = None
    Tasa: Optional[str] = None
    Tipoprestamo: Optional[str] = None
    Codigoprestamo: Optional[str] = None
    Amortizacion: Optional[str] = None
    Diasvencpago: Optional[str] = None
    Diasgracias: Optional[str] = None
    Cargosintereses: Optional[str] = None
    Mto_max_prestamo: Optional[str] = None
    Mto_max_acc: Optional[str] = None
    Mto_cuota_maxima: Optional[str] = None
    Mto_max_ah: Optional[str] = None

class CondicionesTcModel(BaseModel):
    Marca: Optional[str] = None
    Tipo: Optional[str] = None
    Limite: Optional[str] = None
    PlazoMinimo: Optional[str] = None
    Grupoafin: Optional[str] = None
    Adelantoefectivo: Optional[str] = None
    AdelantoCuota: Optional[str] = None
    Bonificacionrenovacion: Optional[str] = None
    Bonificacionresumen: Optional[str] = None
    Mto_max_tc_visa: Optional[str] = None
    Mto_max_tc_master: Optional[str] = None
    Mto_upgrade_tc_visa: Optional[str] = None
    Mto_upgrade_tc_master: Optional[str] = None

class DocumentacionModel(BaseModel):
    Documento1: Optional[str] = None
    Documento2: Optional[str] = None
    Documento3: Optional[str] = None
    Documento4: Optional[str] = None
    Documento5: Optional[str] = None
    Vigenciadoc1: Optional[str] = None
    Vigenciadoc2: Optional[str] = None
    Vigenciadoc3: Optional[str] = None
    Vigenciadoc4: Optional[str] = None
    Vigenciadoc5: Optional[str] = None

class VerificacionesModel(BaseModel):
    Verificacion_1: Optional[str] = None
    Verificacion_2: Optional[str] = None
    Verificacion_3: Optional[str] = None
    Verificacion_4: Optional[str] = None

class NivelDeFirmeModel(BaseModel):
    Descripcion_1: Optional[str] = None
    Descripcion_2: Optional[str] = None
    Descripcion_3: Optional[str] = None
    Codigo_1: Optional[str] = None
    Codigo_2: Optional[str] = None
    Codigo_3: Optional[str] = None

class PrebureauFinalModel(BaseModel):
    Cf: Optional[FillerModel] = None
    Ci: Optional[FillerModel] = None
    IndexacionDeDatos: Optional[PrebureauSubRutina] = None
    Score: Optional[PrebureauScore] = None
    FiltrosDuros: Optional[PrebureauFiltros] = None
    LlamarABuro: Optional[LlamarABuroModel] = None

class EvaluacionFinalModel(BaseModel):
    Ci: Optional[VarNumTextModel] = None
    IndexacionDeDatos: Optional[VarNumTextExtendedModel] = None
    ScoreDeOriginacion: Optional[Any] = None # Scoring
    NivelDeRiesgo: Optional[DescripcionCodigoModel] = None
    IngresoInferido: Optional[Any] = None # Process
    ClasificacionCliente: Optional[DescripcionCodigoModel] = None
    Endeudamiento: Optional[EndeudamientoModel] = None
    CapacidadDePago: Optional[Any] = None # Capacidadpago
    ExposicionMensual: Optional[ExposicionMensualModel] = None
    ExposicionGlobal: Optional[ExposicionGlobalModel] = None
    CondicionPrestamos: Optional[CondicionPrestamosModel] = None
    CondicionesTc: Optional[CondicionesTcModel] = None
    Politicas: Optional[PoliticasResultModel] = None
    Documentacion: Optional[DocumentacionModel] = None
    Verificaciones: Optional[VerificacionesModel] = None
    NivelDeFirme: Optional[NivelDeFirmeModel] = None
    CalculosFinales: Optional[VarNumTextModel] = None

class ResultadoModel(BaseModel):
    Prebureau: Optional[PrebureauFinalModel] = None
    Evaluacion: Optional[EvaluacionFinalModel] = None
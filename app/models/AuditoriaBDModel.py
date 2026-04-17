from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AuditoriaBD(Base):
    __tablename__ = 'auditoria'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_consulta = Column(DateTime, server_default=func.now())
    cuit = Column(String(11))
    nombre_endpoint = Column(String(100))
    estado_consulta = Column(String(10))
    request_data = Column(JSONB)
    response_data = Column(String)



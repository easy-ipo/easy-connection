from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from Models.EnderecoDoador import EnderecoDoador
from Models.EnderecoRequisitante import EnderecoRequisitante

Base = declarative_base()


class Requisitante(Base):
    __tablename__ = 'requisitante'

    cod_requisitante = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    cnpj = Column(String(18))
    cpf = Column(String(14))
    codigo_end_req = Column(Integer, ForeignKey(EnderecoRequisitante.cod_end_req), nullable=False)

    endereco_requisitante = relationship(EnderecoRequisitante)

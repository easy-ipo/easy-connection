from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from Models.Alimentos import Alimentos
from Models.Doador import Doador
from Models.Requisitante import Requisitante

Base = declarative_base()


class Doacoes(Base):
    __tablename__ = 'doacoes'

    cod_doacao = Column(Integer, primary_key=True, autoincrement=True)
    cod_doador = Column(Integer, ForeignKey(Doador.cod_doador), nullable=False)
    cod_requisitante = Column(Integer, ForeignKey(Requisitante.cod_requisitante), nullable=False)
    cod_alimento = Column(Integer, ForeignKey(Alimentos.cod_alimento), nullable=False)
    qnt_peso = Column(Numeric, nullable=False)

    doador = relationship(Doador)
    requisitante = relationship(Requisitante)
    alimento = relationship(Alimentos)

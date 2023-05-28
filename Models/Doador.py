from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from Models.EnderecoDoador import EnderecoDoador

Base = declarative_base()


class Doador(Base):
    __tablename__ = 'doador'

    cod_doador = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    cnpj = Column(String(18))
    cpf = Column(String(14))
    cod_end_doador = Column(Integer, ForeignKey(EnderecoDoador.cod_end_doador), nullable=False)
    pontuacao = Column(Integer, nullable=False)

    endereco_doador = relationship(EnderecoDoador)

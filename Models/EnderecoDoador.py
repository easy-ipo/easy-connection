from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class EnderecoDoador(Base):
    __tablename__ = 'endereco_doador'

    cod_end_doador = Column(Integer, primary_key=True, autoincrement=True)
    logradouro = Column(String(80), nullable=False)
    numero = Column(Integer, nullable=False)
    cep = Column(String(9), nullable=False)
    bairro = Column(String(30), nullable=False)
    uf = Column(String(2), nullable=False)
    municipio = Column(String(30), nullable=False)

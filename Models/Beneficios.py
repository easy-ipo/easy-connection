from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Beneficios(Base):
    __tablename__ = 'beneficios'

    cod_beneficio = Column(Integer, primary_key=True, autoincrement=True)
    nome_beneficio = Column(String(50), nullable=False)
    pontuacao_minima = Column(Integer, nullable=False)

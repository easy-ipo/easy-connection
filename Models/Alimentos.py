from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from Models.Pontuacao import Pontuacao

Base = declarative_base()


class Alimentos(Base):
    __tablename__ = 'alimentos'

    cod_alimento = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80), nullable=False)
    categoria = Column(String(50))
    cod_pontuacao = Column(Integer, ForeignKey(Pontuacao.cod_pontuacao), nullable=False)

    pontuacao = relationship(Pontuacao)

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pontuacao(Base):
    __tablename__ = 'pontuacao'

    cod_pontuacao = Column(Integer, primary_key=True, autoincrement=True)
    pontuacao = Column(Integer, nullable=False)

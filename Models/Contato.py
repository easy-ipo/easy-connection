from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contato(Base):
    __tablename__ = 'contato'

    cod_contato = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(40), nullable=False)
    email = Column(String(30), nullable=False)
    mensagem = Column(String(255), nullable=False)
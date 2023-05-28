from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Noticias(Base):
    __tablename__ = 'noticias'

    cod_noticia = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    conteudo = Column(Text, nullable=False)

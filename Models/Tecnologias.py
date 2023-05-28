from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tecnologias(Base):
    __tablename__ = 'tecnologias'

    cod_tecnologia = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    conteudo = Column(Text, nullable=False)
    imagem = Column(String(255))

from Services.ConnectionService import ConnectionService

from Models.Alimentos import Alimentos, Base as AlimentosBase
from Models.Beneficios import Beneficios, Base as BeneficiosBase
from Models.Contato import Contato, Base as ContatoBase
from Models.Doacoes import Doacoes, Base as DoacoesBase
from Models.Doador import Doador, Base as DoadorBase
from Models.EnderecoDoador import EnderecoDoador, Base as EnderecoDoadorBase
from Models.EnderecoRequisitante import EnderecoRequisitante, Base as EnderecoRequisitanteBase
from Models.Noticias import Noticias, Base as NoticiasBase
from Models.Pontuacao import Pontuacao, Base as PontuacaoBase
from Models.Requisitante import Requisitante, Base as RequisitanteBase
from Models.Tecnologias import Tecnologias, Base as TecnologiasBase


class DatabaseService:
    def __init__(self):
        self.connection = ConnectionService()
        self.connection.connect()

    def create_database(self):
        NoticiasBase.metadata.create_all(bind=self.connection.engine)
        TecnologiasBase.metadata.create_all(bind=self.connection.engine)
        PontuacaoBase.metadata.create_all(bind=self.connection.engine)
        AlimentosBase.metadata.create_all(bind=self.connection.engine)
        BeneficiosBase.metadata.create_all(bind=self.connection.engine)
        ContatoBase.metadata.create_all(bind=self.connection.engine)
        EnderecoDoadorBase.metadata.create_all(bind=self.connection.engine)
        DoadorBase.metadata.create_all(bind=self.connection.engine)
        EnderecoRequisitanteBase.metadata.create_all(bind=self.connection.engine)
        RequisitanteBase.metadata.create_all(bind=self.connection.engine)
        DoacoesBase.metadata.create_all(bind=self.connection.engine)

    def get_all(self, model):
        return self.connection.session.query(model).all()

    def get_by_id(self, model, id):
        return self.connection.session.query(model).get(id)

    def get_by(self, model, **kwargs):
        return self.connection.session.query(model).filter_by(**kwargs).all()

    def get_one_by(self, model, **kwargs):
        return self.connection.session.query(model).filter_by(**kwargs).first()

    def add(self, model):
        self.connection.session.add(model)
        self.connection.session.commit()

    def update(self, model):
        self.connection.session.merge(model)
        self.connection.session.commit()

    def delete(self, model):
        self.connection.session.delete(model)
        self.connection.session.commit()

    def disconnect(self):
        self.connection.disconnect()
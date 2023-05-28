import os
import cx_Oracle
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


class ConnectionService:

    def __init__(self):
        load_dotenv()
        oracle_client = os.getenv('ORACLE_CLIENT')
        username = os.getenv('DB_USERNAME')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        sid = os.getenv('DB_SID')
        service_name = os.getenv('DB_SERVICE_NAME')
        cx_Oracle.init_oracle_client(oracle_client)
        if service_name != '':
            self.engine = sqlalchemy.create_engine(f"oracle+cx_oracle://{username}:{password}@{host}:{port}?service_name={service_name}&encoding=UTF-8")
        else:
            self.engine = sqlalchemy.create_engine(f"oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}?encoding=UTF-8&nencoding=UTF-8")
        self.Session = sessionmaker(bind=self.engine)

    def engine(self):
        return self.engine

    def connect(self):
        self.session = self.Session()

    def disconnect(self):
        self.session.close()

    def execute_query(self, query):
        result = self.session.execute(query)
        return result.fetchall()

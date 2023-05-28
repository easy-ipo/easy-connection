from Services.DatabaseService import DatabaseService

print("Easy Connection a sua plataforma de doações de alimentos")

database_service = DatabaseService()

print("Iniciando a criação do banco de dados...")

database_service.create_database()
database_service.disconnect()

print("Criação do banco de dados concluída com sucesso")
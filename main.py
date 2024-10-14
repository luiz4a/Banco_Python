import os 

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dadps 
MEU_BANCO = create_engine ("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker (bind=MEU_BANCO)
session = Session()


#criando tabela 

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    #Definindo campos da tabela 
    id = Column ("Id", Integer, primary_key=True, autoincrement=True)
    nome = Column ("nome", String)
    email = Column("email", String )
    senha = Column ("Senha", String)

    #Definindo atributos da classe 
    def __init__(self, nome:str, email: str, senha: str):
        self.nome =  nome 
        self.email = email 
        self.senha = senha  

#Criando tabela no banco de Dados 
Base.metadata.create_all(bind=MEU_BANCO)

#CRUD 
#Create - Insert - Salvar 

os .system("cls||clear")

print("Solicitando dados para o usuario. ")
inserir_nome = input("DIgite seu nome: ")
inserir_email = input("Digite seu e-mail: ")
inserir_senha = input("DIgite sua senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()

# Read - Select - Consulta 
print("\nExibindo Dados De todos os clientes na tabela")
lista_clientes = session.query(Cliente). all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

#U - Update - UPDATE - Atualizar
print("\n Atualizando dados do usuario.")
email_cliente = input ("Diogite o email do cliente que sera atualzado: ")

cliente =session.query(Cliente).filter_by(email= email_cliente).first()

if cliente: 
    cliente.nome = input("DIgite seu nome: ")
    cliente.email = input("Digite seu e-mail: ")
    cliente.senha = input("DIgite sua senha: ")

    session.commit()
else: 
    print("Cliente não encontrado.")


# R - Read - Select - Consulta 

print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")


# D - Delete -DELETE - Excluir 
print("\nExcluindo os dados de um cliente.")
email_cliente = input("Digite o email do cliente que sera excluido: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome} Excluido com sucesso!")
else:
    print("Cliente não encontrado.")

# R - Read - Select - Consulta 

print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# R - Read - SELECT - Consulta 
print("Consultando os dado de apenas um cliente")
email_cliente  = input(" Digite o email do CLiente:  ")
cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
else:
    print("Cliente não ecnontrado!")

#Fechando conexão
session.close()


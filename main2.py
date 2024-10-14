import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados 
# 
# 
BANCO_2 = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=BANCO_2)
session = Session()

# Criando tabela 
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "clientes"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    r_a = Column ("ra", String)
    nome = Column("nome", String)
    sobrenome = Column ("Sobrenome", String)
    email = Column("email", String)
    senha = Column("Senha", String)

    def __init__(self, r_a: str, nome: str,sobrenome: str,  email: str, senha: str):
        self.r_a = r_a
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha  

# Criando tabela no banco de Dados 
Base.metadata.create_all(bind=BANCO_2)

def clear_console():
    os.system("cls||clear")

def solicitar_dados_cliente():
    print("Solicitando dados para o usuário.")
    r_a = input ("Digite seu R.A: ")
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    return Aluno(r_a = r_a ,nome=nome, sobrenome = sobrenome,  email=email, senha=senha)

def exibir_clientes():
    print("\nExibindo dados de todos os clientes na tabela")
    lista_clientes = session.query(Aluno).all()
    for cliente in lista_clientes:
        print(f"{cliente.id} -{cliente.r_a} - {cliente.nome}- {cliente.sobrenome} - {cliente.email} - {cliente.senha}")

def atualizar_cliente(email_cliente):
    cliente = session.query(Aluno).filter_by(email=email_cliente).first()
    if cliente:
        cliente.nome = input("Digite seu nome: ")
        cliente.email = input("Digite seu e-mail: ")
        cliente.senha = input("Digite sua senha: ")
        session.commit()
    else:
        print("Aluno não encontrado.")

def excluir_cliente(email_cliente):
    cliente = session.query(Aluno).filter_by(email=email_cliente).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        print(f"Cliente {cliente.nome} excluído com sucesso!")
    else:
        print("Cliente não encontrado.")

def consultar_cliente(email_cliente):
    cliente = session.query(Aluno).filter_by(email=email_cliente).first()
    if cliente:
        print(f"{cliente.id} -{cliente.r_a} - {cliente.nome}- {cliente.sobrenome} - {cliente.email} - {cliente.senha}")
    else:
        print("Aluno não encontrado!")

def main():
    clear_console()

    # Create
    cliente = solicitar_dados_cliente()
    session.add(cliente)
    session.commit()

    exibir_clientes()


    #U - Update - UPDATE - Atualizare
    print("\nAtualizando dados do usuário.")
    email_cliente = input("Digite o email do cliente que será atualizado: ")
    atualizar_cliente(email_cliente)

    exibir_clientes()

    # Delete
    print("\nExcluindo os dados de um cliente.")
    email_cliente = input("Digite o email do cliente que será excluído: ")
    excluir_cliente(email_cliente)

    exibir_clientes()

  # R - Read - SELECT - Consulta especifica 
    print("Consultando os dados de apenas um cliente")
    email_cliente = input("Digite o email do Cliente: ")
    consultar_cliente(email_cliente)

    # Fechando conexão
    session.close()
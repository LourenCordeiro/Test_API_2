from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey      #Comando para criar o motor do banco de dados e os tipos de dados
from sqlalchemy.orm import declarative_base             #Cria a base do banco de dados
from sqlalchemy_utils.types import ChoiceType             #Cria o ChoiceType que é um tipo de dados que permite escolher entre um conjunto de valores, nesse caso os valores são PENDENTE, CANCELADO, FINALIZADO


#Cria conexão com o banco de dados
db = create_engine("sqlite:///banco.db")  #Criando o banco de dados no paretese vai o caminho do banco de dados local ou link do banco de dados

#Cria a base do banco de dados
Base = declarative_base()

#Cria as classes/tabelas do banco de dados
#Usuário
class Usuario(Base):
    __tablename__ = "usuarios"    #Por padrão a tabela é o nome da classe em minusculo e no plural (usuarios) mas também pode ser definido manualmente com o comando "__tablename__"

    id = Column("id", Integer, primary_key=True, autoincrement=True)    #O ID é o número único de casa usuário(primary key) e o autoincrement=True é para que o ID seja incrementado automaticamente
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo =Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)    #Nesse caso o default é para que o admin seja False por padrão e se não for definido o valor é False ou seja o usuário é comum por padrão

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

#Pedido
class Pedido(Base):
    __tablename__ = "pedidos"

    #STATUS_PEDIDO = (
    #    ("PENDENTE", "PENDENTE"),
    #    ("CANCELADO", "CANCELADO"),
    #    ("FINALIZADO", "FINALIZADO")
    #)

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)   #pendente, cancelado, finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id"))       #Nessa informação está ligando o usuario ao pedido através do ID do usuarios, ForeignKey é para ligar a tabela usuario ao pedido
    preco = Column("preco", Float)
    #itens = 

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

#Itens do Pedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True) 
    quantidade = Column("quantidade", Integer) 
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#Executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)
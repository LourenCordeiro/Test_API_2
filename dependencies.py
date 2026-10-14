from sqlalchemy.orm import sessionmaker
from models import db

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)    #Cria a conexão com o banco de dados
        session = Session()                         #Cria a sessão com o banco de dados
        yield session
    finally:                                        #Vai executar o finally mesmo que aconteça um erro(independente do resultado)
        session.close()
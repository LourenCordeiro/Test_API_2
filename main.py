#uvicorn main:app --reload (rodar sempre que o arquivo for alterado ou o arquivo for iniciado para que seja sempre atualizado)
from fastapi import FastAPI
from passlib.context import CryptContext     #Contexto para criptografar a senha do usuário
from dotenv import load_dotenv          #Carrega as variáveis de ambiente do arquivo .env
import os                                #Importa o módulo os para manipular as variáveis de ambiente

load_dotenv()        #Carrega as variáveis de ambiente do arquivo .env

SECRET_KEY = os.getenv("SECRET_KEY")
 #Após carregar e comunicar a secret key, vamos criar o contexto para criptografar a senha do usuário através do CryptContext

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")    #Cria o contexto para criptografar a senha do usuário através do CryptContext

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)





# endpoint:
# /ordens

#\CRUD\ Rest APIs: Get(leitura/pegar), Post(enviar/criar), Put/Patch(edição) e Delete(deletar)  -> tipo de requisições que podem ser feitas na API
#CRUD é utilizado para gerenciar os dados da API(banco de dados)




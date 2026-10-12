#uvicorn main:app --reload (rodar sempre que o arquivo for alterado ou o arquivo for iniciado para que seja sempre atualizado)
from fastapi import FastAPI

from auth_routes import auth_router
from order_routes import order_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)





# endpoint:
# /ordens

#\CRUD\ Rest APIs: Get(leitura/pegar), Post(enviar/criar), Put/Patch(edição) e Delete(deletar)  -> tipo de requisições que podem ser feitas na API
#CRUD é utilizado para gerenciar os dados da API(banco de dados)




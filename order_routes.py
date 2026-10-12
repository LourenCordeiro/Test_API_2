from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")          #definir o caminho e o tipo de requisição (DECORATOR)
async def pedidos():                   #Atribuir a função (async é utilizado para que a função seja assíncrona)
    return {"mensagem": "Você acessou a rota de pedidos"}
    
from fastapi import APIRouter

#é importante sempre definir um préfixo para as rotas para que seja mais organizado e facil de entender, nesse caso será "auth"
#É importante criar tags para que seja fácil de entender a separação das rotas, nesse caso terá "auth" e "order"

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def atenticar():
    """
    Essa é a  rota padrão de autenticação de pedidos do nosso sistema
    """
    return {"mensagem": "Você acessou a rota de autenticação", "autenticado": False}
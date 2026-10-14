from fastapi import APIRouter, Depends
from dependencies import pegar_sessao
from sqlalchemy.orm import Session
from schemas import PedidoSchema
from models import Pedido


order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")          #definir o caminho e o tipo de requisição (DECORATOR)
async def pedidos():                   #Atribuir a função (async é utilizado para que a função seja assíncrona)
    return {"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")    #definir o caminho e o tipo de requisição (DECORATOR)
#a rota nesse caso é: dominio/pedidos/pedido 
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):    
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso! ID do pedido: {novo_pedido.id}"}

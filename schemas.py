#Pydantic é uma biblioteca para validação de dados, força a tipagem de dados.É utilizado com o objetivo de garantir velocidade e integridade dos dados.
from pydantic import BaseModel
from typing import Optional


class UsuarioSchema(BaseModel):  #Schema para validação de dados do usuário.
    nome : str
    email: str
    senha :str
    ativo: Optional[bool]
    admin: Optional[bool] 

    class Config:
        from_attributes = True    #Permite que o pydantic trabalhe com o sqlalchemy, convertendo os dados para o tipo de dado esperado.


class PedidoSchema(BaseModel):  #Schema para validação de dados do pedido.
    usuario: int             #id do usuário que está fazendo o pedido (foi definido no models.py)

    class Config: 
        from_attributes = True    #Permite que o pydantic trabalhe com o sqlalchemy, convertendo os dados para o tipo de dado esperado.


class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True
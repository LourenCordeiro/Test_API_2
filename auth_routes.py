from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema, LoginSchema

#é importante sempre definir um préfixo para as rotas para que seja mais organizado e facil de entender, nesse caso será "auth"
#É importante criar tags para que seja fácil de entender a separação das rotas, nesse caso terá "auth" e "order"

auth_router = APIRouter(prefix="/auth", tags=["auth"])


def criar_token(email):             #Função para criar o token JWT (não é o mais seguro, mas é para fins de teste)
    token = f"sdfsdfaskmkmdd{email}"
    return token


@auth_router.get("/")
async def home():
    """
    Essa é a  rota padrão de autenticação de pedidos do nosso sistema
    """
    return {"mensagem": "Você acessou a rota de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session = Depends(pegar_sessao)):   #Esse comando está puxando a função pegar_sessao (arquivo dependencies.py) para criar a sessão com o banco de dados 
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()    #Faz uma consulta no banco de dados para verificar se o email já existe 
    if usuario:
        #Se achou o usuário é porque já tem esse mesmo email cadastrado
        raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado")
    else:
        #Não existe esse email cadastrado, será possível criar a conta
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)         #Criptografa em hash a senha do usuário 
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)       #Adiciona o novo usuário ao banco de dados
        session.commit()             #Salva as alterações no banco de dados
        return {"mensagem":"Conta criada com sucesso", "usuario": novo_usuario.email}

#login -> email senha -> token JWT (JSON web token) -> resposta com o token -> token é usado para autenticar o usuário em todas as requisições subsequentes.
@auth_router.post("/login")
async def login(login_schema: LoginSchema,  session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==login_schema.email).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    else:
        access_token = criar_token(usuario.id)
        # JWT bearer
        return {
            "access_token":access_token,  #token de acesso
            "token_type": "Bearer"        #tipo de token
            }


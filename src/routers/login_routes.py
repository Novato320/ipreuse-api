from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/")
def home():
    """
    Essa é a rota padrão de autenticação da API
    """
    return {"mensagem": "Acessou rota padrão de autenticação"}

@router.post("/criar_conta")
def criar_conta(email: str, senha: str):
    pass

@router.post("/logar")
def logar(email: str, senha: str):
    pass
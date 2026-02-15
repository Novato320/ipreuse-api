import os

from fastapi import FastAPI
from .routers import login,catalogo,testes
from .database.comand_supabase import init_supabase, consultar_banco
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

app = FastAPI()

app.include_router(login.router)
app.include_router(catalogo.router)


app.include_router(testes.router)


"""
@app.on_startup()
def teste():
    pass

@app.on_event()
def teste():
    pass

@app.lifespan()
def teste():
    pass
"""

@app.get("/banco")
def banco():
    init_supabase(url, key)
    return consultar_banco()
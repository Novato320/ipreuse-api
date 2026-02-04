import os

from fastapi import FastAPI
from .routers import users, items
from .db import comand_supabase
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/banco")
def banco():
    comand_supabase.init_supabase(url, key)
    return comand_supabase.consultar_banco()
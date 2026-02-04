from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client | None = None


def init_supabase(url: str, key: str):
    global supabase
    supabase = create_client(url, key)


def consultar_banco():
    if supabase is None:
        raise RuntimeError("Supabase não inicializado")

    response = (
        supabase.table("users")
        .select("*")
        .execute()
    )
    return response
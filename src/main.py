from typing import Union

#from banco import consultar_banco
from supabase import create_client, Client

url: str = "https://hkdmjetyhvepudotkcjr.supabase.co"
key: str = "sb_publishable_GoINKSbl3Y_5J7N5lXhBWA_8RQfkJ6T"
supabase: Client = create_client(url, key)

def consultar_banco():
    response = (
        supabase.table("users")
        .select("*")
        .execute()
    )

    return response

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return consultar_banco()
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


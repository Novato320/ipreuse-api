from fastapi import APIRouter

router = APIRouter(prefix="/testes", tags=["Testes"])

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}

"""
@router.on_startup()
def teste():
    print("Olá")

@router.on_event()
def teste():
    pass

@router.lifespan()
def teste():
    pass
"""

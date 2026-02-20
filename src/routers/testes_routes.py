from fastapi import APIRouter, Depends

router = APIRouter(prefix="/testes", tags=["Testes"])

def funcao_qualquer():
    try:
        yield {"mensagem": "olá"} # com return ele não volta para essa função e o finally não executa
    finally:
        print("Acabou a função qualquer")

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}

@router.get("/depedencia/{item_id}")
def get_item(item_id: int, dependencia = Depends(funcao_qualquer)):
    """
    Essa função usa o recurso de dependencias do fastapi
    """
    dict1 = {"id": item_id}
    dict2 = dependencia

    dict3 = dict1 | dict2
    dict4 = dict1.update(dict2) # muda o dict1 mas não salva no dict4
    dict5 = {**dict1, **dict2}

    print(dict3)
    print(dict4)
    print(dict5)

    return dict5

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

from fastapi import APIRouter

router = APIRouter(prefix="/catalogo", tags=["Catalogo"])

@router.get("/")
def get_ips():
    return [{"id": "124352", "nome": "alfonso"},{"id": "122", "nome": "juh"},{"id": "352", "nome": "rone"}]


@router.get("/{ip_id}")
def get_ip(ip_id: int):
    return {"id": "352", "nome": "rone"}

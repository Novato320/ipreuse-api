from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users():
    return []

@router.on_startup()
def teste():
    pass

@router.on_event()
def teste():
    pass

@router.lifespan()
def teste():
    pass
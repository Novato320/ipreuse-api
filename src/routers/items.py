from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}

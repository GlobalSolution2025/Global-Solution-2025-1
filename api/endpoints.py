from typing import Optional
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    """
    Endpoint principal.
    Retorna uma mensagem de boas-vindas.
    """
    return {"message": "Hello, World"}

@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    """
    Endpoint que retorna o item pelo ID.
    
    Parâmetros:
    - item_id: ID do item (int)
    - q: query opcional (str)
    """
    return {"item_id": item_id, "q": q}

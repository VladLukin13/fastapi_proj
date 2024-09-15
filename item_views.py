from fastapi import Path, APIRouter
from typing import Annotated

router = APIRouter(prefix="/item", tags=["Items"])


@router.get("/")
def get_list_items():
    return [
        "Item",
        "Item2",
        "Item3",
    ]


@router.get("/{item_id}")
def get_lid_item(item_id: Annotated[int, Path(ge=1, lt=1234)]):
    return {
        "Item": {
            "id": item_id,
        },
    }

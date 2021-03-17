from uuid import uuid4
from fastapi import APIRouter

router = APIRouter()


@router.post("")
async def train():
    return {"model": "dummy", "task": uuid4(), "state": "pending"}

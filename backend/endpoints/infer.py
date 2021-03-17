from fastapi import APIRouter

router = APIRouter()


@router.post("")
async def predict():
    return {"model": "dummy", "value": 0}

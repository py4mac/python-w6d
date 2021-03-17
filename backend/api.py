from fastapi import APIRouter

from backend.endpoints import infer, train

api_router = APIRouter()
api_router.include_router(infer.router, prefix="/predict", tags=["Prediction"])
api_router.include_router(train.router, prefix="/train", tags=["Train"])

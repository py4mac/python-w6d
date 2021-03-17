import uvicorn
from fastapi import FastAPI
from backend.api import api_router

server = FastAPI(
    title="W6D",
    docs_url="/api/v1/doc",
    version="v1",
    description="API"
)

server.include_router(
    api_router, prefix="/api/v1",
)

if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=80)

from app.config import get_config
from fastapi import FastAPI
from app.api.api_v1.api import api_router_v1, PREFIX_V1

import uvicorn


app = FastAPI()
config = get_config()


app.include_router(api_router_v1, prefix=PREFIX_V1)


def start():
    """
    Launched with 'poetry run start' at root level
    """
    uvicorn.run(
        app=config.APP,
        host=config.HOST,
        port=config.PORT,
        reload=config.RELOAD,
        workers=config.WORKERS,
    )

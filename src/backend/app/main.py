from app.config import get_config
from fastapi import FastAPI
from app.api.api_v1.api import api_router

import uvicorn


app = FastAPI()
config = get_config()


app.include_router(api_router, prefix=config.API_PREFIX)


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

from app.config import config
from fastapi import FastAPI  # , HTTPException
# from starlette.responses import Response
import uvicorn


app = FastAPI()


@app.get("/")
def root():
    """
    Hello World root path
    """
    return {"message": "Fast API in Python"}


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

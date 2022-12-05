from app.config import Settings
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
        app=Settings.app,
        host=Settings.host,
        port=Settings.port,
        reload=Settings.reload,
        workers=1,
    )

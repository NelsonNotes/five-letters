import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    environ = str(os.environ['ENVIRON'])
    app = str(os.environ['APP'])
    host = str(os.environ['HOST'])
    port = int(os.environ['PORT'])
    reload = bool(os.environ['RELOAD'])
    workers = int(os.environ['WORKERS'])

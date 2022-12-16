# import os
# from dotenv import load_dotenv

# load_dotenv()


# class Settings:
#     environ = str(os.environ['ENVIRON'])
#     app = str(os.environ['APP'])
#     host = str(os.environ['HOST'])
#     port = int(os.environ['PORT'])
#     reload = bool(os.environ['RELOAD'])
#     workers = int(os.environ['WORKERS'])
import secrets
from functools import lru_cache
from pydantic import BaseSettings, Field, BaseModel


class AppConfig(BaseModel):
    """Application configurations."""


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # These variables will be loaded from the .env file. However, if
    # there is a shell environment variable having the same name,
    # that will take precedence.

    APP_CONFIG = AppConfig()

    # define global variables with the Field class
    ENVIRON: str = Field('dev', env="ENVIRON")

    # environment specific variables do not need the Field class
    APP: str = "app.main:app"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM = "HS256"

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"


class DevConfig(GlobalConfig):
    """Development configurations."""
    HOST: str = "localhost"
    PORT: int = 9090
    RELOAD: bool = True
    WORKERS: int = 1
    DATABASE_URI: str

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"


class ProdConfig(GlobalConfig):
    """Production configurations."""
    HOST: str = "0.0.0.0"
    PORT: int = 9090
    RELOAD: bool = False
    WORKERS: int = 4
    DATABASE_URI: str

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"


class FactoryConfig:
    """Returns a config instance dependending on the ENV_STATE variable."""

    def __init__(self, env_state: str):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()
        elif self.env_state == "prod":
            return ProdConfig()
        else:
            raise ValueError('ENVIRON must be only "dev" or "prod"')


@lru_cache
def get_config() -> DevConfig | ProdConfig:
    settings = FactoryConfig(GlobalConfig().ENVIRON)()
    return settings

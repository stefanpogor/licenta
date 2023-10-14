import os
from dotenv import load_dotenv


def load_environment_vars():
    env = os.environ.get("FLASK_ENV", "development")

    if env=="production":
        load_dotenv("config/config.prod.env")
    else:
        load_dotenv("config/config.dev.env")

load_environment_vars()
FLASK_ENV = os.environ.get("FLASK_ENV")
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")

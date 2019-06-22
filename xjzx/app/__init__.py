from flask import Flask

from app import settings
from app.ext import init_app
from app.urls import init_urls


def create_app(env):
    app=Flask(__name__)

    app.config.from_object(settings.config_env.get(env))

    init_app(app)

    init_urls(app)

    return app
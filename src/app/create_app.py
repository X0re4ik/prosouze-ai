from fastapi import FastAPI

from src.routes import app_route


def create_app() -> FastAPI:
    app = FastAPI(
        title="App",
        description="App",
        version="1.0.0",
    )

    app.include_router(
        app_route,
    )

    return app

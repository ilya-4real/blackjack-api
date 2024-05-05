from fastapi import FastAPI

from app.application.auth.router import router as auth_router


def get_app() -> FastAPI:
    app = FastAPI(
        title="simple application for blackjack game",
        docs_url="/docs",
    )
    app.include_router(auth_router)
    return app

from fastapi import FastAPI


def get_app() -> FastAPI:
    app = FastAPI(
        title="simple application for blackjack game",
        docs_url="/docs",
    )
    return app

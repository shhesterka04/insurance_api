from fastapi import FastAPI

from src.router import insurance_router


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(insurance_router)
    return application


app = get_application()

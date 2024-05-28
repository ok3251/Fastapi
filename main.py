# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.app_router import page_router

def include_router(app):
    app.include_router(page_router)

def start_application():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    include_router(app)
    return app

app = start_application()

    
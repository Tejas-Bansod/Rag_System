from fastapi import FastAPI
from services.api_gateway.routes.chat import router

app = FastAPI(title="Document AI")

app.include_router(router)

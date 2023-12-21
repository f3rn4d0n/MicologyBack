from fastapi import FastAPI
from app.api.endpoints import settings, receipts, welcomePage

app = FastAPI()
app.title = settings.appName
app.version = settings.apiVersion

app.include_router(welcomePage.router, prefix="", tags=["home"])
app.include_router(settings.router, prefix="", tags=["appState"])
app.include_router(receipts.router, prefix="", tags=["recipes"])

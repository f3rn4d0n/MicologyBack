from fastapi import FastAPI
from app.api.endpoints import settings, receipts, welcomePage
#from app.api.data.database import database, metadata

app = FastAPI()
app.title = settings.appName
app.version = settings.apiVersion

#@app.on_event("startup")
#async def startup_db_client():
#    await database.connect()

#@app.on_event("shutdown")
#async def shutdown_db_client():
#    await database.disconnect()

app.include_router(welcomePage.router, prefix="", tags=["home"])
app.include_router(settings.router, prefix="", tags=["appState"])
app.include_router(receipts.router, prefix="", tags=["recipes"])

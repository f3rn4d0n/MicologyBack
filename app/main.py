from fastapi import FastAPI
from app.api.endpoints import settings, receipts, welcomePage, cocktails
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

app.include_router(welcomePage.router, prefix="", tags=["Home"])
app.include_router(settings.router, prefix="", tags=["AppState"])
app.include_router(receipts.router, prefix="", tags=["Recipes"])
app.include_router(cocktails.router, prefix="", tags=["Cocktails"])

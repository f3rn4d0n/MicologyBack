from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/") 
def home():
    return HTMLResponse('<h1>Cocktails</h1>')
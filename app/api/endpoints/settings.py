from fastapi import APIRouter
from enum import Enum

router = APIRouter()
appName = "Cocktail Api"
apiVersion = "0.0.3"

# Enum to represent the available cocktail types
class AppStateType(str, Enum):
    READY = "ready"
    MAINTAIN = "maintain"
    ERROR = "error"
   
@router.get("/appState") 
async def get_appState():
  return {
    "state": AppStateType.READY.value,
    "sdkVersion" : apiVersion,
    "appVersion": {
     "iOS": "1.0.0",
     "Android": "1.0.0" 
    }  
  }
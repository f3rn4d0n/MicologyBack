from fastapi import APIRouter, HTTPException
from enum import Enum

router = APIRouter()
appName = "Cocktail Api"
apiVersion = "0.0.3"

# Enum to represent the available cocktail types
class AppStateType(str, Enum):
    READY = "ready"
    MAINTAIN = "maintain"
    ERROR = "error"
    
class AppSupportedPlatforms(int, Enum):
    WebView = 0
    Android = 1
    iOS = 2
   
@router.post("/appState") 
async def get_appState(platform: int):
  if platform == AppSupportedPlatforms.iOS:
    return {
      "state": AppStateType.READY.value,
      "sdkVersion": apiVersion,
      "appVersion": "1.0.0",
      "platform": "iOS"
    }
  elif platform == AppSupportedPlatforms.Android:
    return {
      "state": AppStateType.READY.value,
      "sdkVersion": apiVersion,
      "appVersion": "1.0.0",
      "platform": "Android"
    }
  elif platform == AppSupportedPlatforms.WebView:
    return {
      "state": AppStateType.READY.value,
      "sdkVersion": apiVersion,
      "webVersion": "1.0.0",
      "platform": "WebView"
    }
  else:
    raise HTTPException(status_code=404, detail="Unknow platform")
import sys
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from enum import Enum

app = FastAPI()
app.title = "Cocktail Api"
app.version = "0.0.2"

# Specify the path to your JSON file
json_file_path = 'app/defaultCocktails.json'

# Enum to represent the available cocktail types
class AppStateType(str, Enum):
    READY = "ready"
    MAINTAIN = "maintain"
    ERROR = "error"

@app.get("/", tags=['home'])
def home():
    return HTMLResponse('<h1>Recipes</h1>')
  
@app.get("/appState", tags=['app'])
def get_appState():
  return {
    "state": AppStateType.READY.value,
    "sdkVersion" : app.version,
    "appVersion": {
     "iOS": "1.0.0",
     "Android": "1.0.0" 
    }  
  }

@app.get("/recipes", tags=['recipes'])
def get_recipes():
  # Read the JSON content from the file
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    return recipes

@app.get("/recipes/{id}", tags=['recipes'])
def get_recipe(id: int):
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    cocktails = recipes["cocktails"]
    cocktail = list(filter(lambda x: x['id'] == id, cocktails))
    if len(cocktail) > 0:
        return cocktail[0] 
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.get("/recipes/search/", tags=['recipes'])
async def get_movies_by_name(ingredient: str):
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    # Crear una lista para almacenar las recetas que cumplen con la condición
    recetas_encontradas = []

    # Iterar a través de las recetas
    for cocktail in recipes["cocktails"]:
        # Verificar si el ingrediente está en la lista de ingredientes
        if ingredient.lower() in [ingrediente.lower() for ingrediente in cocktail["ingredients"]]:
            recetas_encontradas.append(cocktail)

    # Devolver la lista de recetas que cumplen con la condición
    return recetas_encontradas

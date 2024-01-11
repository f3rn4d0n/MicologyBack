from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
#from sqlalchemy.ext.asyncio import AsyncSession
from app.api.data import models, crud
from app.api.data.models import Cocktail
#from app.api.data.database import database, metadata
from pydantic import Field
import json

router = APIRouter()

# Specify the path to your JSON file
json_file_path = 'app/api/resources/defaultCocktails.json'

listRecipes = []

@router.get("/recipes") 
async def get_recipes():
  # Read the JSON content from the file
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    return JSONResponse(content=recipes)

@router.get("/recipes/{id}") 
async def get_recipe(id: str):
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    cocktails = recipes["cocktails"]
    cocktail = list(filter(lambda x: x['id'] == id, cocktails))
    if len(cocktail) > 0:
        return JSONResponse(content=cocktail[0])
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.get("/recipes/find/{ingredient}") 
async def get_recipes_by_ingredient_or_tag(ingredient: str):
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    recetas_encontradas = [cocktail for cocktail in recipes["cocktails"]
                       if ingredient.lower() in map(str.lower, cocktail["ingredients"]) or
                       ingredient.lower() in map(str.lower, cocktail.get("tags", []))]
    if len(recetas_encontradas) > 0:
        return recetas_encontradas 
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.get("/cocktail")
async def get_cocktail(): 
  return listRecipes
  
@router.post("/cocktail")
async def create_cocktail(cocktail: Cocktail): 
  listRecipes.append(cocktail)
  return cocktail
  
  
@router.put("/cocktail/{item_id}")
async def update_cocktail(item_id: int, cocktail: Cocktail): 
  listRecipes[item_id] = cocktail
  return cocktail
  
@router.delete("/cocktail/{item_id}")
async def delete_cocktail(item_id: int): 
  del listRecipes[item_id]
  return {"message": "Item deleted"}
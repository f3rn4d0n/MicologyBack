from fastapi import APIRouter, HTTPException
import json

router = APIRouter()

# Specify the path to your JSON file
json_file_path = 'app/api/resources/defaultCocktails.json'

@router.get("/recipes") 
async def get_recipes():
  # Read the JSON content from the file
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    return recipes

@router.get("/recipes/{id}") 
async def get_recipe(id: str):
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    cocktails = recipes["cocktails"]
    cocktail = list(filter(lambda x: x['id'] == id, cocktails))
    if len(cocktail) > 0:
        return cocktail[0] 
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.post("/recipes/find") 
async def get_recipes_by_ingredient_or_tag(ingredient: str):
  with open(json_file_path, 'r') as file:
    recipes = json.load(file)
    recetas_encontradas = [cocktail for cocktail in recipes["cocktails"]
                       if ingredient.lower() in map(str.lower, cocktail["ingredients"]) or
                       ingredient.lower() in map(str.lower, cocktail.get("tags", []))]
    if len(recetas_encontradas) > 0:
        return recetas_encontradas 
    raise HTTPException(status_code=404, detail="Recipe not found")

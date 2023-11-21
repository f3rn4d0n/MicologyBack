import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Cocktail Api"
app.version = "0.0.1"

recipes = {
  "cocktails": [
    {
        "id": 1,
      "name": "Mojito",
      "ingredients": ["mint leaves", "lime", "simple syrup", "white rum", "soda water", "ice cubes"],
      "recipe": [
        "Muddle mint leaves and lime in a glass.",
        "Add simple syrup and white rum.",
        "Top up with soda water and stir.",
        "Add ice cubes and garnish with a mint sprig."
      ],
      "history": "The Mojito is a traditional Cuban cocktail that dates back to the 16th century."
    },
    {
        "id": 2,
      "name": "Martini",
      "ingredients": ["gin", "dry vermouth", "lemon twist or olive"],
      "recipe": [
        "Chill the glass by placing it in the freezer or filling it with ice water.",
        "In a mixing glass, combine gin and dry vermouth with ice.",
        "Stir or shake well, then strain into the chilled glass.",
        "Garnish with a lemon twist or olive."
      ],
      "history": "The Martini is a classic cocktail with disputed origins, believed to have originated in the late 19th century."
    },
    {
        "id": 3,
      "name": "Margarita",
      "ingredients": ["tequila", "triple sec", "lime juice", "salt for rimming"],
      "recipe": [
        "Rub the rim of the glass with the lime wedge to moisten it.",
        "Dip the rim in salt to coat it.",
        "In a shaker with ice, combine tequila, triple sec, and lime juice.",
        "Shake well and strain into the glass over ice."
      ],
      "history": "The Margarita is a popular Mexican cocktail with a disputed origin, possibly dating back to the 1930s."
    },
    {
        "id": 4,
      "name": "Old Fashioned",
      "ingredients": ["bourbon or rye whiskey", "sugar cube", "angostura bitters", "orange twist"],
      "recipe": [
        "Place the sugar cube in a glass and saturate it with bitters.",
        "Muddle the sugar and bitters together.",
        "Add a large ice cube and pour the whiskey over it.",
        "Stir gently and garnish with an orange twist."
      ],
      "history": "The Old Fashioned is a classic cocktail that dates back to the early 19th century."
    },
    {
        "id": 5,
      "name": "Negroni",
      "ingredients": ["gin", "sweet vermouth", "Campari", "orange slice or twist"],
      "recipe": [
        "Fill a glass with ice cubes.",
        "Pour equal parts gin, sweet vermouth, and Campari over the ice.",
        "Stir well and garnish with an orange slice or twist."
      ],
      "history": "The Negroni is an Italian cocktail that originated in Florence, Italy, in the early 20th century."
    },
    {
        "id": 6,
      "name": "Cosmopolitan",
      "ingredients": ["vodka", "triple sec", "cranberry juice", "lime juice", "orange twist"],
      "recipe": [
        "Fill a shaker with ice cubes.",
        "Add vodka, triple sec, cranberry juice, and lime juice to the shaker.",
        "Shake well and strain into a chilled martini glass.",
        "Garnish with an orange twist."
      ],
      "history": "The Cosmopolitan gained popularity in the 1990s and is often associated with cosmopolitan cities like New York."
    },
    {
        "id": 7,
      "name": "Whiskey Sour",
      "ingredients": ["bourbon or rye whiskey", "simple syrup", "lemon juice", "orange slice or cherry"],
      "recipe": [
        "Fill a shaker with ice cubes.",
        "Add whiskey, simple syrup, and lemon juice to the shaker.",
        "Shake well and strain into a rocks glass filled with ice.",
        "Garnish with an orange slice or cherry."
      ],
      "history": "The Whiskey Sour is a classic cocktail that dates back to the mid-19th century."
    },
    {
        "id": 8,
      "name": "Piña Colada",
      "ingredients": ["white rum", "coconut cream", "pineapple juice", "pineapple slice and maraschino cherry for garnish"],
      "recipe": [
        "Fill a blender with ice cubes.",
        "Add white rum, coconut cream, and pineapple juice to the blender.",
        "Blend until smooth and pour into a chilled glass.",
        "Garnish with a pineapple slice and maraschino cherry."
      ],
      "history": "The Piña Colada is a tropical cocktail that originated in Puerto Rico in the 1950s."
    },
    {
        "id": 9,
      "name": "Gin and Tonic",
      "ingredients": ["gin", "tonic water", "lime wedge or slice"],
      "recipe": [
        "Fill a glass with ice cubes.",
        "Pour gin over the ice and top up with tonic water.",
        "Stir gently and garnish with a lime wedge or slice."
      ],
      "history": "The Gin and Tonic is a classic cocktail that originated in British colonial India as a way to mask the bitter taste of quinine in tonic water."
    }
  ]
}

@app.get("/", tags=['home'])
def home():
    return HTMLResponse('<h1>Recipes</h1>')

@app.get("/recipes", tags=['recipes'])
def get_recipes():
    return recipes

@app.get("/recipes/{id}", tags=['recipes'])
def get_recipe(id: int):
    cocktails = recipes["cocktails"]
    cocktail = list(filter(lambda x: x['id'] == id, cocktails))
    if len(cocktail) > 0:
        return cocktail[0] 
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.get("/recipes/search/", tags=['recipes'])
async def get_movies_by_name(ingredient: str):
    # Crear una lista para almacenar las recetas que cumplen con la condición
    recetas_encontradas = []

    # Iterar a través de las recetas
    for cocktail in recipes["cocktails"]:
        # Verificar si el ingrediente está en la lista de ingredientes
        if ingredient.lower() in [ingrediente.lower() for ingrediente in cocktail["ingredients"]]:
            recetas_encontradas.append(cocktail)

    # Devolver la lista de recetas que cumplen con la condición
    return recetas_encontradas

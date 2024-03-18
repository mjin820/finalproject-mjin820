import requests
import keys

def get_recipes(meal_type, max_calories):
    base_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "type": meal_type,
        "maxCalories": max_calories,
        "addRecipeInformation": True,
        "addRecipeNutrition": True,
        "sort": "calories",
        "sortDirection": "asc",
        "apiKey": keys.MY_SECRET_API_KEY
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        recipes = data.get("results", [])
        for recipe in recipes:
            calories = recipe.get('nutrition', {}).get('calories')
            recipe['calories'] = calories
        return recipes
    else:
        print("Error retrieving recipes:", response.status_code)
        return None


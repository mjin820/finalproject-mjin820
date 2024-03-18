# finalproject-mjin820
My final project (3-Step Meal Planner) for HCDE 310 Winter Quarter 2024. 

I created a 3-Step Meal Planner where the user can choose a meal type (breakfast, main course, or dessert) and their desired number of calories. Once the user clicks on the "Search Recipes" button, a new page will be generated with a variety of meal options and recipes that meet those criteria. In each recipe card, the recipe title is displayed as well as an image of the meal, serving size, total time required, and a link to the full recipe. 

Installation Process:
1. Clone the repository
2. Install dependencies using pip install -r requirements.txt
3. This project uses an API key from Spoonacular. The code imports a file called keys.py (create a new file called keys.py) into functions.py with the parameter "apiKey": keys.MY_SECRET_API_KEY. The keys.py file was added to .gitignore and will require an API key to be included in keys.py in this format: MY_SECRET_API_KEY = 'your_api_key_here'. To obtain an API key, go to https://spoonacular.com/food-api/console#Dashboard, sign up for an account, go to MY CONSOLE --> Profile --> Generate New API key
4. To run Flask app: python app.py --> and access the application in your web browser

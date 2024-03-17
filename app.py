from flask import Flask, render_template, request
import functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    meal_type = request.form['meal_type']
    max_calories = request.form['max_calories']

    if not meal_type or not max_calories:
        return 'Please provide meal type and maximum number of calories per serving'

    try:
        max_calories = int(max_calories)
    except ValueError:
        return 'Maximum calories must be a number'

    recipes = functions.get_recipes(meal_type, max_calories)
    return render_template('results.html', recipes=recipes, meal_type=meal_type, max_calories=max_calories)

if __name__ == '__main__':
    app.run(debug=True)

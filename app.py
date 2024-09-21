from flask import Flask, render_template, request
from db_connection import connect_db
from models import insert_user_profile, fetch_food_items

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = int(request.form['age'])
    health_condition = request.form['health_condition']
    daily_calories = int(request.form['daily_calories'])

    
    connection, cursor = connect_db()
    insert_user_profile(cursor, name, age, health_condition, daily_calories)
    connection.commit()

    
    foods = fetch_food_items(cursor, health_condition)
    connection.close()


    return render_template('result.html', foods=foods, health_condition=health_condition)

if __name__ == "__main__":
    app.run(debug=True)

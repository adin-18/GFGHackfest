from models import fetch_food_items

def recommend_meal(cursor, health_condition):
    # Fetch food items suitable for the user's health condition
    foods = fetch_food_items(cursor, health_condition)

    print(f"Recommended meals for {health_condition}:")
    for food in foods:
        print(f"{food[1]} - {food[2]} calories, {food[3]}g protein, {food[4]}g fat, {food[5]}g carbs")

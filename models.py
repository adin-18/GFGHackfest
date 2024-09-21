def insert_user_profile(cursor, name, age, health_condition, daily_calories):
    query = """
    INSERT INTO health_profiles (name, age, health_condition, daily_calories)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, age, health_condition, daily_calories))

def fetch_food_items(cursor, health_condition):
    query = f"SELECT * FROM food_items WHERE suitable_for = '{health_condition}'"
    cursor.execute(query)
    return cursor.fetchall()

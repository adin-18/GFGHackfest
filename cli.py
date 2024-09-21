def get_user_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    # Ask the user to select a health condition
    print("Select your health condition from the following:")
    print("1. Diabetes")
    print("2. Hypertension (High Blood Pressure)")
    print("3. Obesity")
    print("4. Anemia")
    
    health_conditions = ['Diabetes', 'Hypertension', 'Obesity', 'Anemia']
    health_condition_choice = int(input("Enter the number corresponding to your health condition: "))
    health_condition = health_conditions[health_condition_choice - 1]
    
    daily_calories = int(input("Enter your daily calorie requirement: "))
    
    return name, age, health_condition, daily_calories

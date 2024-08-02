
def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return bmr

def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories


while True:

    print("\n\n============== Calorie Tracker Calculator App ==============")

    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    age = int(input("Enter your age: "))
    sex = input("Enter your sex (male or female): ")
    activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active): ")

    bmr = calculate_bmr(weight, height, age, sex)
    calories = calculate_daily_calories(bmr, activity_level)

    print("Your daily calorie needs are: ", calories)
    
    input("\n\nPress Enter to continue...")
    cont = input("Try another one? Press Y to continue & N to exit: ")
    while cont.lower() not in ("y","n"):
        cont = input("Try another one? Press Y to continue & N to exit: ")
    if cont == "n":
        break

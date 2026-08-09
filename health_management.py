while True:
    print("====================================")

    print("        PERSONAL HEALTH SYSTEM         ")

    print("====================================")

    print("1. create a profile")
    print("2. BMI calculator")
    print("3. calorie tracker")  
    print("4. water tracker")
    print("5. workout manager")
    print("6. food planner ")
    print("7. cycle tracker")
    print("8.exit")


    choice = input("enter an option:  ")

    if choice == "1":
        print("====================================")

        print("         CREATE PROFILE             ")

        print("====================================")   

        name = input("enter your name: ")
        age = int(input("enter your age: "))
        gender = input("enter your gender: ")
        height = float(input("enter your height in cm: "))        
        weight = float(input("enter your weight in kg: "))

        print("profile created succesfully!")



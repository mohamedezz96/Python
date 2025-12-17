while True:
    try:
        age = int(input("Please enter your age: "))
        break   # exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a numeric value for age.")

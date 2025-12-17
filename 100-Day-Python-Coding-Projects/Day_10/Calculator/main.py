import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero.")
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
descesion = "n"
while descesion == "n":
    clear()
    print("Welcome To The Calculator")
    first_number = float(input("Enter The First Number: "))
    descesion = "y"
    print("Choose The Operation: ")

    while descesion == "y":
        for operation in operations:
            print(operation)

        operation_choice = input("Your Choice: ")
        second_number = float(input("Enter The Second Number: "))

        if operation_choice == "+":
            print(f"The Result:  {first_number} {operation_choice} {second_number} = {add(first_number, second_number)}")
            first_number = add(first_number, second_number)     
        elif operation_choice == "-":
            print(f"The Result:  {first_number} {operation_choice} {second_number} = {subtract(first_number, second_number)}")
            first_number = subtract(first_number, second_number)
        elif operation_choice == "*":
            print(f"The Result:  {first_number} {operation_choice} {second_number} = {multiply(first_number, second_number)}")
            first_number = multiply(first_number, second_number)
        elif operation_choice == "/":
            print(f"The Result:  {first_number} {operation_choice} {second_number} = {divide(first_number, second_number)}")
            first_number = divide(first_number, second_number)

        descesion = input(f"If you want to continue with {first_number} type (y) if you want to start new calculation type (n): ")    
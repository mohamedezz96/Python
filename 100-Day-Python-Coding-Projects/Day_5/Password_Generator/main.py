import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

print("Welcome To The Password Generator!")

number_of_capital_letters= int(input("How many capital letters would you like in your password? "))
number_of_small_letters = int(input("How many small letter would you like in your password? "))
number_of_numbers = int(input("How many numbers would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like in your password? "))

password_combination = []

for i in range(0, number_of_capital_letters):
    password_combination.append(capital_letters[random.randint(0, len(capital_letters)-1)])

for i in range(0,number_of_small_letters):
    password_combination.append(small_letters[random.randint(0, len(small_letters)-1)])

for i in range(0, number_of_numbers):
    password_combination.append(numbers[random.randint(0, len(numbers)-1)])

for i in range(0, number_of_symbols):
    password_combination.append(symbols[random.randint(0, len(symbols)-1)])

random.shuffle(password_combination)

passoword = ""

for character in password_combination:
    passoword += character

print(f"Your Password: {passoword}")

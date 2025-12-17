logo = """
  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               
"""

import random, os

def easy(random_number):
    number_of_atttempts = 10
    print(f"You have {number_of_atttempts} attempts!")
    for i in range (0, 10):
        user_guess = int(input("Make a Guess: "))
        if user_guess == random_number:
            print("N!CE, You Got It!")
            return 
        elif user_guess > random_number:
            print("Too High!")
            number_of_atttempts -= 1
            print(f"You have {number_of_atttempts} attempts!")
        elif user_guess < random_number:
            print("Too Low!")
            number_of_atttempts -= 1
            print(f"You have {number_of_atttempts} attempts!")

    print(f"Bad Luck!, You didn't Got It. The Number is {random_number}")

        

def hard(random_number):
    number_of_atttempts = 5
    print(f"You have {number_of_atttempts} attempts!")
    for i in range (0, 5):
        user_guess = int(input("Make a Guess: "))
        if user_guess == random_number:
            print("N!CE, You Got It!")
            return 
        elif user_guess > random_number:
            print("Too High!")
            number_of_atttempts -= 1
            print(f"You have {number_of_atttempts} attempts!")
        elif user_guess < random_number:
            print("Too Low!")
            number_of_atttempts -= 1
            print(f"You have {number_of_atttempts} attempts!")

    print(f"Bad Luck!, You didn't Got It. The Number is {random_number}")




print(logo)
print("Welcome To The Number Guessing Game!")
print("I'm Thinking Of Number Between 1 : 100")
random_number = random.randint(1, 100)
difficulty = input("Choose Difficulty (Easy/Hard): ").lower()

if difficulty == "easy":
    easy(random_number)

elif difficulty == "hard":
    hard(random_number)

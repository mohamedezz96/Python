import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors: "))
computer_choice = random.randint(0,2)

if user_choice == computer_choice:
    print(f"user:\n{game_options[user_choice]}")
    print(f"computer:\n{game_options[computer_choice]}")
    print("Draw")
else:
    if user_choice == 0 and computer_choice == 1:
        print(f"user:\n{game_options[user_choice]}")
        print(f"computer:\n{game_options[computer_choice]}")
        print("Computer Win!")

    elif user_choice == 0 and computer_choice == 2:
        print(f"user:\n{game_options[user_choice]}")
        print(f"computer:\n{game_options[computer_choice]}")
        print("You Win!")

    elif user_choice == 1 and computer_choice == 0:
        print(f"user:\n{game_options[user_choice]}")
        print(f"computer:\n{game_options[computer_choice]}")
        print("You Win!")

    elif user_choice == 1 and computer_choice == 2:
        print(f"user:\n{game_options[user_choice]}")
        print(f"computer:\n{game_options[computer_choice]}")
        print("Computer Win!")

    elif user_choice == 2 and computer_choice == 0:
        print(f"user:\n{game_options[user_choice]}")
        print(f"computer:\n{game_options[computer_choice]}")
        print("Computer Win!")

    elif user_choice == 2 and computer_choice == 1:
        print(f"user:\n{game_options[user_choice]}")
        print(f"computer:\n{game_options[computer_choice]}")
        print("You Win!")

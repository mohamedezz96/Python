print("Welcome To Treasure Island.")
print("Your Mission Is To Find The Treasure.")

choice = input("Left or Right? ").lower()

if choice == "left":
    choice = input("Swim or Wait? ").lower()
    if choice == "wait":
        choice = input("Which Door? (Red - Blue - Yellow) ").lower()
        if choice == "yellow":
            print("You Win!")
        elif choice == "red":
            print("Burned by fire, GameOver!")
        elif choice == "blue":
            print("Eaten by beasts, GameOver!")
        else:
            print("GameOver!")
    else:
        print("Attacked by trout, GameOver!")
else:
    print("Fall Into a Hole, GameOver!")

import random 
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []
player_sum = 0
dealer_sum = 0
player_action = ""
end_game = False

for i in range(0,2):
    dealer.append(random.choice(cards))

for i in range(0,2):
    player.append(random.choice(cards))

initial_player_sum = player[0] + player[1]

print(f"Your Cards Are [{player[0]}, {player[1]}] With Sum: {initial_player_sum}")
print(f"Dealer Cards Are [{dealer[0]}, *] With Sum: {dealer[0]} ")

if player_sum == 21:
    print("BlackJack!, You Won!")
else:
    player_action = input("stand / hit? ").lower()
    while player_action == "hit" and end_game == False:
        player.append(random.choice(cards))
        for score in player:
            player_sum += score
        print(f"Your Cards Are: {player} With Sum: {player_sum}")
        print(f"Dealer Cards Are: [{dealer[0]}, *]  with Sum: {dealer[0]}")
        if player_sum >21:
            if 11 in player:
                player.remove(11)
                player.append(1) 
                player_sum = 0
                for score in player:
                    player_sum += score
            else:            
                print("Bust!, You Lost")
                end_game = True
        else:
            player_action = input("stand / hit? ").lower()
    if end_game == False:
        while dealer_sum < 17:
            dealer.append(random.choice(cards))
            for score in dealer:
                dealer_sum += score
            print(f"Dealer Cards Are: {dealer} With Sum: {dealer_sum}")
            if dealer_sum > 21:
                if 11 in dealer:
                    dealer.remove(11)
                    dealer.append(1)
                    dealer_sum = 0
                    for score in dealer:
                        dealer_sum += score
                else:
                    print("You Won!")
                    end_game = True
        if end_game == False:
            print(f"Dealer Cards Are: {dealer} With Sum: {dealer_sum}")
            print(f"Your Cards Are: {player} With Sum: {player_sum}")

            if player_sum == 21 and dealer_sum != 21:
                print("You Won!")
            elif player_sum > dealer_sum:
                print("You Won!")
            elif player_sum == dealer_sum:
                print("Draw!")
            elif dealer_sum > player_sum:
                print("Dealer Won!")
    

            




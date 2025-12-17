import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


BANNER = r"""
  ____  _     _ _     _   _                       _             
 |  _ \(_) __| (_)___| |_| |__   ___  _   _ _ __ | |_ ___  _ __ 
 | |_) | |/ _` | / __| __| '_ \ / _ \| | | | '_ \| __/ _ \| '__|
 |  _ <| | (_| | \__ \ |_| | | | (_) | |_| | |_) | || (_) | |   
 |_| \_\_|\__,_|_|___/\__|_| |_|\___/ \__,_| .__/ \__\___/|_|   
                                           |_|                  
             Blind (sealed-bid) Auction
"""

print(BANNER)
print("Welcome to the Secret Auction Program.")

stop = False
name_bid_dict = {}

while not stop:
    name = input("What Is Your Name? ")
    bid = int(input("What Is Your Bid? $"))
    clear()
    name_bid_dict[name] = bid
    action = input("Is there anyone want to bid? (Yes/No) ").lower()
    clear()
    if action == "no":
        stop = True

max_bid_name = max(name_bid_dict, key=name_bid_dict.get)
max_bid = name_bid_dict[max_bid_name]
print(f"The winner is {max_bid_name} with bid ${max_bid}")

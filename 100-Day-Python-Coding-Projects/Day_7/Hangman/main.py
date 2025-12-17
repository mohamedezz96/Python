import random

logo = """
 _                                            
| |                                           
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

words_list = [
    "python",
    "variable",
    "hangman",
    "programming",
    "function",
    "loop",
    "devops",
    "cloud",
    "docker",
    "engineer",
    "telephone",
    "football",
    "sunshine",
    "laptop",
    "keyboard",
]

stages = [
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]

print (logo)

word = random.choice(words_list)
word_list = []
blank = "_" * len(word)
blank_list = []

trials = 0

for char in word:
    word_list.append(char)

for char in word:
    blank_list.append("_")

print(f"Guess The Word: {blank} ({len(blank)} character)")

while "_" in blank_list and trials < 7:
    user_input = input("Guess a char in the word: ")
    if user_input in word_list:
        for i in range(0,len(word_list)):
            if user_input == word_list[i]:
                blank_list[i] = user_input
                word_list[i] = "*"
        print(f"Correct! {''.join(blank_list)}")
    else:
        trials += 1
        print(stages[-trials])
        print(f"Incorrect! {''.join(blank_list)}")
        print(f"You have {7 - trials} trials left.")
        
if "_" in blank_list:
    print("GameOver! You Dead.")
else:
    print("Congratulations! You Got It")

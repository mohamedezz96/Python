user_input_1 = input("Enter your first word: ").replace(" ","").lower()
user_input_2 = input("Enter your second word: ").replace(" ","").lower()
if len(user_input_1) == len(user_input_2):
    user_input_1_list = list(user_input_1)
    user_input_2_list = list(user_input_2)
    user_input_1_list.sort()
    user_input_2_list.sort()
    if user_input_1_list == user_input_2_list:
        print("Anagrams")
    else:
        print("Not Anagrams")
else:
    print("Not Anagrams")

user_input_1 = input("Enter Your Word: ")
user_input_2 = input("Enter Your sequence of letters: ")
final_result = True
result = 0 
for char in user_input_1:
    result = user_input_2.find(char, result)
    if result == -1:
        final_result = False
        break
    else:
        result += 1

if final_result:
    print("Yes")
else:
    print("No")

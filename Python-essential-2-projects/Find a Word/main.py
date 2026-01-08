user_input_1 = input("Enter Your Word: ")
user_input_2 = list(input("Enter Your sequence of letters: "))
length_check = len(user_input_1)

for char in user_input_1:
    if char in user_input_2:
        length_check -= 1

if length_check == 0:
    print("Yes")
else:
    print("No")
  

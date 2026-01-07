user_input = input("Enter Your Birthday in that format MMDDYYYY: ")
user_input_list = list(user_input)
user_input_sum = 0
for digit in user_input_list:
    user_input_sum += int(digit)
    
while user_input_sum > 10:
    user_input_sum = str(user_input_sum)
    user_input_list = list(user_input_sum)
    user_input_sum = 0 
    for digit in user_input_list:
        user_input_sum += int(digit)
        
print(user_input_sum)

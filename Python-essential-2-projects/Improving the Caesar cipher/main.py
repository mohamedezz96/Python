user_text_input = input("Enter The Text You Want To Encrypt: ")
user_shift_number = int(input("Enter Shift Value You Want (1-25): "))
encrypted_message = ""

for char in user_text_input:
    if char == " " or char.isdigit():
        encrypted_message += char
    elif char.islower():
        if (ord(char) + user_shift_number) <= 122:
            encrypted_message += chr(ord(char) + user_shift_number)
        else:
            encrypted_message += chr(ord(char) + user_shift_number - 26)
    elif char.isupper():
        if (ord(char) + user_shift_number) <= 90:
            encrypted_message += chr(ord(char) + user_shift_number)
        else:
            encrypted_message += chr(ord(char) + user_shift_number - 26)       
            
        
print(encrypted_message)

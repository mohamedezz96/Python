user_input = input("Enter Your Text: ").replace(" ","").lower()
reversed_text = user_input[::-1]

if user_input == reversed_text:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

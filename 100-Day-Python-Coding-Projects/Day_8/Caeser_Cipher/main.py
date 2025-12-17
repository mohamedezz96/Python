alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(text, shift):
    encoded_text = []
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            if (char_index + shift) <= (len(alphabet)-1):
                encoded_text.append(alphabet[(char_index + shift)])
            else:
                encoded_text.append(alphabet[(shift-(25-char_index))-1])
        else:
            encoded_text.append(char)

    print(f"Your encrypted text: {''.join(encoded_text)}")

def decrypt(text, shift):
    decoded_text = []
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            if (char_index - shift) >= 0:
                decoded_text.append(alphabet[char_index - shift])
            else:
                decoded_text.append(alphabet[25-(shift - char_index - 1)])
        else:
            decoded_text.append(char)

    print(f"Your text: {''.join(decoded_text)}")

shutdown = False

while not shutdown:
    print("Welcome to the Caesar Cipher Encoder!\nType ''Encode' to Encrypt\nType 'Decode' to Decrypt")
    action = input("Your choice: ").lower()
    text = input("Enter your text you want to encrypt/decrypt: ").lower()
    shift = int(input("Enter the shift number: "))

    if action == "encode":
        encrypt(text, shift)

    elif action == "decode":
        decrypt(text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        shutdown = True
        print("Goodbye!")   

        

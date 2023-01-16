import string

def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    shift_amount = -shift_amount if cipher_direction == "decode" else shift_amount
    for char in start_text:
        if char in string.ascii_lowercase:
            position = ord(char) - ord('a')
            new_position = (position + shift_amount) % 26
            end_text += chr(new_position + ord('a'))
        else:
            end_text += char
    return end_text

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    print(f"Here's the {direction}d result: {caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)}")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() == "no":
        should_end = True
        print("Goodbye")

# This version of the code uses the string module to check if a character is a lowercase letter, and the built-in ord() and 
# chr() functions to convert between characters and their ASCII values. It also uses ternary operator to check for the direction of 
# encryption/decryption, and % operator to wrap around the shift value to the range of alphabets. The while loop also checks for 'no' 
# in lower case to make sure it works for different cases and the print statement at the end is removed since the function already 
# returns the encoded/decoded message.

# Also, you don't need the art library to print the logo, you can print it as plain text.

# This code should work as expected and would be more readable and efficient.

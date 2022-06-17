# I will replicate the Cipher Caesar encode.

# This project is from my python training, so will have a part
# similar to my professor but also my personal touches.

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
# Automate the alphabet
import string
import pyperclip

alpha_gen = string.ascii_lowercase
alphabet = list(alpha_gen + alpha_gen + alpha_gen + alpha_gen + alpha_gen)

# Gathering the inputs and validating
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

while True:
    if direction == 'encode' or direction == 'decode':
        break
    else:
        True
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

while shift >= 104:
    shift = int(input("Type the shift number:\n"))


def caesar(text_input, shift_input):
    text_output = ""
    text_only = ''.join(e for e in text if e.isalnum())
    text_without_space = text_only  # text_input.replace(" ", "")

    for lettler_in_text in text_without_space:
        letter_position = alphabet.index(lettler_in_text)

        if direction == 'encode':
            # Encrypting
            new_position = letter_position + shift_input
        elif direction == 'decode':
            # Dencrypting
            new_position = letter_position - shift_input

        else:
            print("The input it is invalid, try again!")
            exit()

        new_letter_position = alphabet[new_position]

        text_output += new_letter_position

    pyperclip.copy(text_output)
    print(f'The {direction} text is {text_output}')
    print('Copied to clipboard!')

# Calling the function

caesar(text, shift)

# Paint Area Calculator
# import math
# def paint_area_calculator(height, width, cover):
#     area = height * width 
#     total = math.ceil(area / cover)
#     print(f"you'll need {total} cans of paint")
# height_of_wall = int(input("enter Height of Wall: "))
# width_of_wall = int(input("enter Width of wall: "))
# coverage = 5   
# paint_area_calculator(height=height_of_wall, width=width_of_wall, cover=coverage)

# Prime Number Checker

# def prime_checker(number):
#     prime = True
#     for x in range(2, number):
#         if number % x == 0:
#             prime = False
#     if prime:
#         print("it's a prime number")
#     else:
#         print("it's not a prime number")


# n = int(input("check this number: "))
# prime_checker(number=n)

# caesar cipher
## way 1


import string
print(list(string.ascii_lowercase))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt type 'decode' to decrypt:\n")
text = input ("type your message:\n").lower()
shift = int(input("type the shift number:\n"))
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")
      
encrypt(plain_text=text, shift_amount=shift)

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"the decoded text is {plain_text}")
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)





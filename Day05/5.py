# Create a Password Generatar

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the RoboPassword Generator!")
num_letters = int(input("how many letters would you like in your password? "))
num_symbols = int(input("how many symbols would you like? "))
num_numbers = int(input("how many numbers would you like? "))
password = []
for letter in range(1, num_letters + 1):
    password.append(random.choice(letters))
for symbol in range(1, num_symbols + 1):
    password.append(random.choice(symbols))
for number in range(1,num_numbers + 1):
    password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)
main_password = ""
for char in password:
    main_password += char
print(f"your password is: {main_password}")

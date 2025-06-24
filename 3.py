# BMI Calculator

# height = float(input("enter you height in m: "))
# weight = float(input(" enter your weight in kg: "))
# BMI = round(weight / height ** 2)
# if BMI < 18.5:
#     print(f"your BMI is {BMI}, you are under weight.")
# elif BMI < 25:
#     print(f"your BMI is {BMI},you have a normal weight.")
# elif BMI < 30:
#     print(f"your BMI is {BMI},you are overweight.")
# elif BMI < 35:
#     print(f"your BMI is {BMI},you are obese.")
# else:
#     print(f"your BMI is {BMI},you are clinically obese")

# Leap year

# year = int(input("which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

# Bill
# print("Welcome to the rollercoaster!")
# height = int(input("what is your height in cm? "))
# Bill = 0
# if height > 120:
#     print("you can ride the rollercoaster")
#     age = int(input("what is your age? "))
#     if age <12:
#         Bill = 5
#         print("child tickets are $5.")
#     elif age <= 18:
#         Bill = 7
#         print("youth tickets are $7.")
#     else:
#         Bill = 12
#         print("adult tickets are $12.")
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#        Bill += 3
#     print(f"Your final bill is ${Bill}")
# else:
#     print("sorry, you have to grow taller before you can ride")

# Pizza order

# print("Welcome to python pizza deliveries")
# size = input("what size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3   
# if extra_cheese == "Y":
#     bill += 1
# print(f"your final bill is ${bill}") 

# Love Calculator

# print("Welcome to the love calculator!")
# name1 = input("what is your name?\n")
# name2 = input("what is their name?\n")
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
# true = t + r + u + e
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
# love = l + o + v + e
# love_score = int(str(true) + str(love))
# if (love_score < 10) or (love_score > 90):
#     print(f"your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"your score is {love_score}, you are alright together.")
# else:
#     print(f"your score is {love_score}")





import random
from game_data import data
from art import logo
from art import vs


random_personA = random.choice(data)
random_personB = random.choice(data)

print(logo)
score = 0
is_continue = True
while is_continue:
    random_personA = random.choice(data)
    random_personB = random.choice(data) 
    
    compareA = print(f"campare A: {random_personA['name']}, {random_personA['description']}, {random_personA['country']}")
    print(vs)
    againstB = print(f"against B: {random_personB['name']}, {random_personB['description']}, {random_personB['country']}")

    if compareA == againstB:
        random_personB = random.choice(data) 

    more_followers = input("who has more followers? Type 'A' or 'B':\n ")
    if more_followers == "A":
        if random_personA["follower_count"] > random_personB["follower_count"]:
            score += 1
            print(logo)
            print(f"you're right! current score: {score}")
        else:
            print(f"Sorry, that's wrong. final score: {score}")
            is_continue = False
    else:
            print(f"Sorry, that's wrong. final score: {score}")
            is_continue = False

   




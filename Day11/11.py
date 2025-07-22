# blackjack

import random
from art import logo


def get_card():
    cards = [11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def result(your_score, computer_score):
    if your_score == computer_score:
        return "you Draw"
    elif computer_score == 0:
        return "you lose"
    elif your_score == 0:
        return "you win"
    elif your_score > 21:
        return "you lose"
    elif computer_score > 21:
        return "you win"
    elif your_score > computer_score:
        return "you win"
    else:
        return "you lose"
    




def game():
    print(logo)
    your_card = []  
    computer_card = []
    game_over = False
    for numbercard in range(2):
        your_card.append(get_card())
        computer_card.append(get_card())

    while not game_over:
        your_score = score(your_card)
        computer_score = score(computer_card)
        print (f"your cards: {your_card}, current score: {your_score}")
        print(f"computer's first card: {computer_card[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21:
            game_over = True
        else:
            ask_anothercard = input("Type 'y' to get another card, type 'n' to pass: ")
            if ask_anothercard == "y":
                your_card.append(get_card())
            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_card.append(get_card())
        computer_score = score(computer_card)

    print(f"your final hand: {your_card}, final score: {your_score}")
    print(f"computer's final hand: {computer_card}, final score: {computer_score}")
    print(result(your_score, computer_score))

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play_game == "y":
    game() 










        
            





    
    
    















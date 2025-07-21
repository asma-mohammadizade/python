# blackjack

import random
cards = [11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def result():
    if your_finalhand < 21 and com_finalhand < 21:
        if your_finalhand > com_finalhand:
            print("you win")
    elif your_finalhand < 21 and com_finalhand >= 21:
        print("you win")
    elif your_finalhand >= 21 and com_finalhand < 21:
        print("you lose")
    elif your_finalhand == com_finalhand:
        print("you draw")
    else:
        print("you win")


is_continue = True
while is_continue:
    ask_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    if ask_blackjack == "n":
        is_continue = False
    else:
        number1 = random.choice(cards)
        number2 = random.choice(cards)
        com_firstcard = random.choice(cards)
        com_secondcard = random.choice(cards)
        print(f"your cards: [{number1}, {number2}]")
        print(f"computer's first card: {com_firstcard}")
        ask_anothercard = input("Type 'y' to get another card, type 'n' to pass: ")
        if ask_anothercard == "n":
            your_finalhand = number1 + number2
            print(f"your final hand: [{number1}, {number2}]")
            print(f"computer's final hand: [{com_firstcard}, {com_secondcard}]")
            com_finalhand = com_firstcard + com_secondcard
            result()
        else:
            get_anothercards1 = random.choice(cards)
            com_thirdcard = random.choice(cards)
            print(f"your cards: [{number1}, {number2}, {get_anothercards1}]")
            print(f"computer's first card: [{com_firstcard}, {com_secondcard}, {com_thirdcard}]")
            your_finalhand = number1 + number2 + get_anothercards1
            com_finalhand = com_firstcard + com_secondcard + com_thirdcard
            result()
            


    
    
    















# Guess the number

import random
from art import logo

def play_guess_the_number():
    print(logo)
    def hard():
        def result():
            if choose_number > computer_number: 
                print("Too high")
            elif choose_number < computer_number:
                print("Too low")
            else:
                print("correct")

            
        number_of_guess = 5
        for choose_number in range(5):
            print(f"You have {number_of_guess} attempts remaining to guess the number.")
            choose_number = int(input("make a guess: "))
            result()
            number_of_guess -= 1
            if number_of_guess == 0:
                print("you've run out of guesses, you lose")
                


    def easy():
        def result():
            if choose_number > computer_number: 
                print("Too high")
            elif choose_number < computer_number:
                print("Too low")
            else:
                print("correct")
        number_of_guess = 10
        for choose_number in range(10):
            print(f"You have {number_of_guess} attempts remaining to guess the number.")
            choose_number = int(input("make a guess: "))
            result()
            number_of_guess -= 1 
            if number_of_guess == 0:
                print("you've run out of guesses, you lose")



    computer_number = random.randint(1, 100)
    print("Welcom ton the Number Guessing Game!")
    choose_game = input("I'm thinking of a number between 1 and 100.\n choose a difficulty. Type 'easy' or 'hard': ")

    if choose_game == "hard":
        hard()
    else:
        easy()

play_guess_the_number()

play_again = input("Do you want to play again? Type 'yse' or 'no': ")
is_continue = True
if play_again == "yes":
    play_guess_the_number()
else:
    is_continue = False






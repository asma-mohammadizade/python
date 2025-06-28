# Hangman game using python

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["apple", "avocado", "banana","cherry", "pomegranate", "peach", "orange", "melon", "coconut"]
guess_word = random.choice(word_list)
lives = 6
list_letter = []
for letter in guess_word:
    list_letter += "_"
print(list_letter)

end_game = False
while not end_game:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in list_letter:
        print(f"you've already guessed {guess_letter}")

    for n in range(len(guess_word)):
        letter = guess_word[n]
        if letter == guess_letter:
            list_letter[n] = letter
      
    print(list_letter)
   
    if guess_letter not in guess_word:
        print(f"you guessed {guess_letter}, that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("you lose")

    if "_" not in list_letter:
        end_game = True
        print("you win")

    print(stages[lives])
   

"""
Number guessing game

You have 3 tries to guess a number between 1 and 20.
"""
import random

def get_guess(answer):
    guess = int(input("Make a guess: "))

    if answer == guess:
        print('Got it!')
        return True
    elif answer > guess:
        print('Higher')
    elif answer > guess:
        print('Lower')
    return False

def play_game(num_guesses):
    answer = random.randint(1, 20)

    print("I'm thinking of a number between 1 and 20")

    for i in range(num_guesses, 0, -1):
        print(f"You have {i} guess{'' if i == 1 else 'es'} left")

        if get_guess(answer):
            return

    print(f"It was {answer}")

play_game(4)


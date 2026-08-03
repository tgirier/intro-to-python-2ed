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

def play_game():
    answer = random.randint(1, 20)

    print("I'm thinking of a number between 1 and 20")
    
    if get_guess(answer):
        return
    if get_guess(answer):
        return
    if get_guess(answer):
        return

    print(f"It was {answer}")

play_game()

# def check_answer(g, a):
#     if g < a:
#         print("Failed, you're too low!")
#         return False
#     elif g > a:
#         print("Failed you're too high!")
#         return False
#     else:
#         return True

# if check_answer(guess, answer):
#     print("Congratulations you won !")
# else:
#     guess = int(input("Make a guess: "))
#     if check_answer(guess, answer):
#         print("Congratulations you won !")
#     else:
#         guess = int(input("Make a guess: "))
#         if check_answer(guess,answer):
#             print("Congratulations you won !")
#         else:
#             print(f"Failed try again, the answer was {answer}")

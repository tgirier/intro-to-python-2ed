"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""

answers = [
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
]

category = 'Country that starts with V'

guessed = []

# Create a loop with 4 try
while True:
    num_left = len(answers)
    if num_left == 0:
        print("Great Job!")
        break
    print(f"{num_left} left")

# 4 left
    guess = input(f"Enter a {category.lower()} (q to quit): ").title()

    if guess.lower() == "q":
        missed = ', '.join(answers)
        print("You missed: " + missed)
        break
    elif guess in guessed:
        print('Already guessed')
    elif guess in answers:
        guessed.append(guess)
        answers.remove(guess)
        print('Correct')
    else:
        print('Try again')


# Correct!
# Already guessed
# Try again


# Great job!
# You missed: a, b, c, d

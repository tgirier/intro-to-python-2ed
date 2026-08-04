"""
Quiz game

User will try to get all the answers (e.g. countries that start with V)
If they give up and quit, print the ones that were missed
"""
with open('data/V_countries.txt') as file:
    category = file.readline().strip()
    answers = file.read().split('\n')

def get_results(answers_left):
    if len(answers_left) == 0:
        return "Great Job!"
    else:
        missed = ', '.join(answers_left)
        return "You missed: " + missed

def play_game():

    guessed = []
    answers_left = answers.copy()
        
    # Create a loop with 4 try
    while len(answers_left) > 0:
        print(f"{len(answers_left)} left")

    # 4 left
        guess = input(f"Enter a {category.lower()} (q to quit): ").title()

        if guess.lower() == "q":
            break
        elif guess in guessed:
            print('Already guessed')
        elif guess in answers_left:
            guessed.append(guess)
            answers_left.remove(guess)
            print('Correct')
        else:
            print('Try again')

    print(get_results(answers_left))

if __name__ == "__main__":
    play_game()

# Correct!
# Already guessed
# Try again


# Great job!
# You missed: a, b, c, d

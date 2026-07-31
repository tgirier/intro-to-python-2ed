"""
Time target game
"""

# Todo: Create a function that runs a time target game
# Example output:
# 3s test. Hit ENTER to start
# Hit ENTER to stop
# 2.789s
# You were 0.211s off
from random import randint
from time import time

def time_target(t):
    input(f"{t}s test. Hit ENTER to start")
    start = time()
    input("Hit ENTER to stop")
    end = time()

    duration = end - start
    diff = abs(t - duration)

    print(f"{duration:.3}s")
    print(f"You were {diff:.3} off")


# Todo: get random number of seconds
target = randint(2, 5)

# Todo: run game 3 times
time_target(target)
time_target(target)
time_target(target)
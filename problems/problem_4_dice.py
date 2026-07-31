"""
Simulate rolling 2 dice
"""
from random import randint

die_1 = randint(1, 6)
die_2 = randint(1, 6)

print(f"You rolled a {die_1} and {die_2} (total: {die_1 + die_2})")

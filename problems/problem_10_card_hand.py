"""
Deal a hand of 5 cards
"""

import random

suits = ['♠︎', '♣︎', '♥︎', '♦︎']
ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']        

cards = []
hand = []

for suit in suits:
    for rank in ranks:
        cards.append(rank + suit)

for _ in range(5):
    card = random.choice(cards)
    cards.remove(card)
    hand.append(card)

print(cards)
print(hand)

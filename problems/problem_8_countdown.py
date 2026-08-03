"""
Provide a countdown for X seconds, then print "Happy New Year! 🎉"
"""

import time

def countdown(seconds):
    while seconds > 0:
        print(f"{seconds}!")
        seconds -= 1
        time.sleep(1)
    print('Happy New Year! 🎉')


countdown(5)

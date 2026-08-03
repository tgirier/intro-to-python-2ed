"""
Print how many vowels that an input word contains.
"""

word = input("Type a word: ")

vowels_count = 0

for letter in word.lower():
    if letter in 'aeiouy':
        vowels_count +=1

print(f'There are {vowels_count} vowels in "{word}"')

temp = 10

if temp <= 0:
    print("It's freezing")
elif temp < 18:
    print("It's cold")
else:
    print("It's not cold")

if True:
    print('Do something')
print('Always print this')

name = input("What's your name? ")
if name:
    print("Hello "+ name)
else:
    print("Hello World!")

cost = 0

if cost is None:
    print("set a cost")
else:
    print(f"It cost ${cost}")
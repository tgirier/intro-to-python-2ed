# x = 0

# while x <= 10:
#     print(x)
#     x += 1

# x = 0
# while True:
#     print(x)
#     if x == 10:
#         break
#     x += 1

x = -1
while True:
    x += 1
    if x % 2 == 1:
        continue
    print(x)
    if x == 10:
        break
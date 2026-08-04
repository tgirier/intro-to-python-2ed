class MyClass:
    def __init__(self, attr1='hello'):
        self.attr1 = attr1
        self.attr2 = 'B'

    def a_method(self):
        print(f'Called a_method on {self}')

    def __str__(self):
        return f'Instance ({self.attr1}, {self.attr2})'
        
class Horse:
    def __init__(self, colour, age):
        self.age = age
        self.colour = colour

    def trot(self):
        print('clop clop clop clop')

    def __str__(self):
        return f'{self.colour.capitalize()} horse, age {self.age}'

obj = MyClass()
horse1 = Horse('black', 4)
str1 = 'Hello'

print(obj)
print(horse1)
print(type(obj))
print(type(horse1))
obj.a_method()
horse1.trot()

print(obj.attr1)
print(horse1.colour)
# Optional parameters
def add(a, b, precision=8):
    a = float(a)
    b = float(b)
    return round(a + b, precision)


print(add(1, 2))
print(add(1.1, 2.2))
print(add('1.1', '2.2'))
print(add('1.1', '2.2', 20))
print(add('1.1', '2.2', 0))
print(add('1.1', '2.2', None))


# Keyword arguments
def add(a, b):
    a = float(a)
    b = float(b)
    return round(a + b, 8)


print(add(1, 2))
print(add(a=1.1, b=2.2))
print(add('1', b='2'))
print(add(b='1', a='2'))


# Docstrings
def add(a, b):
    """Add two numbers

    a: a number
    b: a number
    return the sum of numbers
    """
    a = float(a)
    b = float(b)
    return round(a + b, 8)


print(add(1, 2))
print(add(1.1, 2.2))
print(add('1', '2'))

help(add)


# Nested functions
def add(a, b):
    def convert(n):
        if isinstance(n, str):
            if n.isnumeric():
                return int(n)
            return float(n)
        return n
    
    a = convert(a)
    b = convert(b)
    return round(a + b, 8)


print(add(1, 2))
print(add(1.1, 2.2))
print(add('1', '2'))


# *args and **kwargs
def add(a, b):
    a = float(a)
    b = float(b)
    return round(a + b, 8)


print(add(1, 2))
print(add(a=1.1, b=2.2))
print(add('1', b='2'))

args = [-1, -2]
kwargs = {'a': '9', 'b': '0.9'}

print(add(*args)) # equivalent of add(-1, -2)
print(add(**kwargs)) # equivalent of add(a='9', b='0.9')

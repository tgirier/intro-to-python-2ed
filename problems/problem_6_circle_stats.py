"""
Given a radius:
  - print the circumference and area of a circle
  - print the surface area and volume of a sphere
"""
from math import pi

def circumference(r):
    return 2 * pi * r


def area(r):
    return pi * r ** 2


def surface_area(r):
    return 4 * pi * r ** 2


def volume(r):
    return 4 / 3 * pi * r ** 3

def get_circle_stats(r):
    print(f'Circle circumference: {circumference(r)}')
    print(f'Circle area: {area(r)}')
    print(f'Sphere surface area: {surface_area(r)}')
    print(f'Sphere volume: {volume(r)}')


radius = float(input("Radius: "))

print(f'Circle circumference: {circumference(radius)}')
print(f'Circle area: {area(radius)}')
print(f'Sphere surface area: {surface_area(radius)}')
print(f'Sphere volume: {volume(radius)}')

get_circle_stats(radius)
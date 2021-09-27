import turtle
from random import *
x = 0
y = 0
for i in range(0, 10000000):
    x = x + randint(-30, 30)
    y = y + randint(-30, 30)
    turtle.goto(x, y)
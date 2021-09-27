import turtle
import math
turtle.shape('turtle')
turtle.speed(0)
pn = 0
a = 0.1
k = math.pi / 180
for i in range(0, 1000000000000000000000000000000000000000000000000):
    pn = pn + a / (2 * math.pi)
    x = pn * math.cos(i * k)
    y = pn * math.sin(i * k)
    turtle.goto(x, y)
while True:
    turtle.left(1)
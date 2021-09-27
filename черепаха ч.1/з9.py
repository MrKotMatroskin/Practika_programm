import turtle
import math
turtle.shape('turtle')
turtle.speed(0)


def krug(r):
    a = math.pi / 45
    shag = 2 * 40 * r * math.sin(a)
    for i in range(0, 45):
        turtle.forward(shag)
        turtle.left(8)
    for i in range(0, 45):
        turtle.forward(shag)
        turtle.right(8)


k = 1
for i in range(1, 100):
    krug(k)
    k = k + 0.2
while True:
    turtle.left(1080)

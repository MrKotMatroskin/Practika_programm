import turtle
import math
turtle.shape('turtle')


def ugolnik(ku, r):
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(90 + 180 / ku)
    shag = r * math.sqrt(2 * (1 - math.cos(2 * math.pi / ku)))
    for i in range(0, ku):
        turtle.forward(shag)
        turtle.left(360 / ku)
    turtle.right(90 + 180 / ku)
    turtle.penup()
    turtle.backward(r)


r = 20
for i in range(3, 40):
    ugolnik(i, r)
    r = r + 10
while True:
    turtle.left(360)

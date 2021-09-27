import turtle
turtle.shape('turtle')
turtle.speed(0)


def krug(n, shag):
    for i in range(0, 45):
        turtle.forward(shag)
        turtle.left(8)
    for i in range(0, 45):
        turtle.forward(shag)
        turtle.right(8)
    turtle.left(360 / n)


k = 3
for i in range(0, k):
    krug(k, 10)
while True:
    turtle.left(1080)

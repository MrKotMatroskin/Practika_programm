import turtle
turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)


def krug(r):
    for i in range(0, 180):
        turtle.forward(r)
        turtle.right(1)
    for i in range(0, 180):
        turtle.forward(r / 4)
        turtle.right(1)


k = 1
for i in range(1, 100):
    krug(k)
while True:
    turtle.left(1080)

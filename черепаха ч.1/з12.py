import turtle
turtle.shape('turtle')
turtle.speed(10)


def z(r, shag):
    turtle.pendown()
    for i in range(0, r):
        turtle.forward(shag)
        turtle.right(180 * ((r - 1) / r))
    turtle.penup()


turtle.penup()
turtle.goto(-400, 0)
z(5, 200)
turtle.forward(500)
z(11, 200)
while True:
    turtle.left(360)

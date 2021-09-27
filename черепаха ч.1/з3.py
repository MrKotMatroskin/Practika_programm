import turtle
turtle.shape('turtle')
turtle.speed(0)
shag = 30
k = 30
for i in range(0, 10):
    for i in range(0, 4):
        turtle.pendown()
        turtle.forward(shag)
        turtle.left(90)
    turtle.penup()
    shag = shag + k
    turtle.backward(k / 2)
    turtle.right(90)
    turtle.forward(k / 2)
    turtle.left(90)
while True:
    turtle.left(1)

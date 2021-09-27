import turtle
turtle.shape('turtle')
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor('yellow')
turtle.circle(120)
turtle.end_fill()

turtle.up()
turtle.goto(-67, -67)
turtle.setheading(-60)
turtle.width(5)
turtle.down()
turtle.circle(80, 120)

turtle.fillcolor('black')

for i in range(-35, 105, 70):
    turtle.up()
    turtle.goto(i, 35)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

while True:
    turtle.left(1080)

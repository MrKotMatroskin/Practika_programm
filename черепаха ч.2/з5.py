import turtle
from random import randint

number_of_turtles = 10
steps_of_the_time_number = 100000

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

for unit in pool:
    unit.turtlesize(0.4)
    unit.penup()
    unit.speed(randint(0, 10))
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.seth(randint(0, 360))
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.goto(200, -200)
turtle.goto(200, 200)
turtle.goto(-200, 200)
turtle.goto(-200, -200)
for i in range(steps_of_the_time_number):
    for g in range(len(pool)):
        ang = pool[g].heading()
        (x, y) = pool[g].pos()
        if x < -200 or x > 200:
            pool[g].seth(180 - ang)
        elif y < -200 or y > 200:
            pool[g].seth(-ang)
        pool[g].fd(5)

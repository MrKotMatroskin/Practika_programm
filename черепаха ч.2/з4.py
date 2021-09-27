import turtle
turtle.shape('turtle')
i = 0
x = -450
y = 0
g = -9.81
Vx = 15
Vy = 50
k = 0
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
for i in range(0, 10):
    while y >= 0:
        k += 1
        t = k / 10000
        x += Vx * t
        y += Vy * t + g * t ** 2 / 2
        Vy += g * t
        if y >= 0:
            turtle.goto(x, y)
        else:
            turtle.goto(x, 0)
    Vx = Vx * 0.75
    Vy = abs(Vy * 0.75)
    y = 0
while True:
    turtle.left(1080)

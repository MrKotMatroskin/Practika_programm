import turtle
turtle.shape('turtle')
turtle.speed(0)
n = 12
for i in range(0, n):
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.left(360 / n)
while True:
    turtle.left(1)
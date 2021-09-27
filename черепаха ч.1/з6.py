import turtle
turtle.shape('turtle')
turtle.speed(10)
a=5
k=5
for i in range(0, 10000000):
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    a=a+k
while True:
    turtle.left(1)
import turtle

space = int(input())
L1 = int(input())
L2 = int(input())
L3 = (L1 ** 2 + L2 ** 2) ** (1/2)
space = space + L2

glyph0 = [(-90, L1), (90, L2), (90, 2*L1), (90, L2), (90, L1)]

glyph1 = [(45, L3), (-135, 2 * L1)]

font = [glyph0, glyph1]

x = int(input())

str = bin(x)[2:]

number = list(map(int, str))

turtle.shape('turtle')
turtle.speed(10)

for digital in number:
    gl = font[digital]
    print(digital)
    for deg, dist in gl:
        turtle.left(deg)
        turtle.forward(dist)
    for deg, dist in gl[::-1]:
        turtle.backward(dist)
        turtle.right(deg)
    turtle.penup()
    turtle.forward(space)
    turtle.pendown()
turtle.done()
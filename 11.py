from turtle import *

xc = int(input("xc = "))
yc = int(input("yc = "))
r = int(input("r = "))
x = int(input("x = "))
y = int(input("y = "))

showturtle()

teleport(xc, yc)
right(90)
penup()
forward(r)
left(90)
pendown()
circle(r)
teleport(x, y)
dot(8, 'red')

d_x = x - xc
d_y = y - yc
color('red')
teleport(xc*2, yc*5)

if (d_x**2 + d_y**2) < r ** 2:
    write("Точка внутри окружности")
else:
    write("Точка вне окружности")
done()
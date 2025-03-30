from turtle import *

k = 20
screensize(1000, 1000)
color("red")
left(90)
tracer(10)

for i in range(9):
  fd(12*k)
  right(90)
  fd(6*k)
  right(90)

penup()
fd(1*k)
right(90)
fd(3*k)
left(90)

pendown()
color("blue")

for i in range(9):
  fd(53*k)
  right(90)
  fd(75*k)
  right(90)


color("black")
penup()
for x in range(-30, 30):
  for y in range(-30, 30):
    goto(x*k, y*k)
    dot(3)

done()
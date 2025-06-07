from turtle import *

screensize(10**6, 10**6)
tracer(100000000000000000000)
left(90)
k = 10
color("red")


right(45)
for i in range(10):
  right(45)
  fd(203*k)
  right(45)

penup()
fd(-40*k)
right(45)
color("blue")
pendown()
for i in range(5):
  fd(20*k)
  left(90)

penup()
for x in range(203, 240):
  for y in range(-150, -203, -1):
    goto(x*k, y*k)
    dot(3, "black")

done()

from turtle import *

k = 20
tracer(0)
screensize(10**6, 10**6)
left(90)
color("red")

for i in range(2):
  fd(5*k)
  right(90)
  fd(11*k)
  right(90)

penup()
fd(-4*k)
right(90)
fd(6*k)
left(90)

pendown()
color("blue")
for i in range(2):
  fd(42*k)
  right(90)
  fd(63*k)
  right(90)

penup()
color("black")

for x in range(-30, 90):
  for y in range(-30, 90):
    goto(x*k,y*k)
    dot(3)

done()
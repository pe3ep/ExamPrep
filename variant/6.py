from turtle import *

screensize(10000, 10000)
color("red")
k = 20
tracer(0)
left(90)

# ---

for i in range(2):
  fd(10*k)
  right(90)
  fd(18*k)
  right(90)

penup()
fd(5*k)
right(90)
fd(7*k)
left(90)

pendown()
color("blue")

for i in range(2):
  fd(10*k)
  right(90)
  fd(7*k)
  right(90)

penup()
color("black")
start = -40
end = 40

for x in range(start, end):
  for y in range(start, end):
    goto(x*k, y*k)
    dot(3)

done()
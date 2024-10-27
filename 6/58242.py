import turtle
import math

zoom = 50
turtle.tracer(0)
turtle.screensize(10000, 10000)
turtle.width(3)

for i in range(4):
  turtle.color("red")
  turtle.forward(4 * (math.sqrt(5)) * zoom)
  turtle.right(150)
  turtle.forward(4 * (math.sqrt(5)) * zoom)
  turtle.right(300)


start = -20
end = 30

turtle.width(1)
turtle.penup()
turtle.color("black")
for x in range(start, end):
  for y in range(start, end):
    turtle.goto(x * zoom, y * zoom)
    turtle.pendown()
  turtle.penup()

for y in range(start, end):
  for x in range(start, end):
    turtle.goto(x * zoom, y * zoom)
    turtle.pendown()
  turtle.penup()

turtle.goto(0,0)
turtle.pendown()

turtle.done()
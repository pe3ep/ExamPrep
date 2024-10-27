# import turtle

# k = 10
# turtle.left(90)
# turtle.tracer(0)
# turtle.screensize(10000, 10000)
# turtle.color("red")

# turtle.right(180)
# turtle.forward(5*k)
# turtle.right(90)
# turtle.forward(50*k)
# turtle.right(90)
# turtle.forward(5*k)

# for i in range(5):
#   turtle.seth(90)
#   turtle.circle(-5 * k, 180)

# turtle.color("black")
# start = -55
# end = 20

# turtle.penup()
# for x in range(start, end):
#   for y in range(start, end):
#     turtle.goto(x * k,y * k)
#     turtle.dot(3)


# turtle.done()

# -----------------------------------------------------

# import turtle

# k = 10
# turtle.left(90)
# turtle.tracer(0)
# turtle.screensize(10000, 10000)
# turtle.color("red")

# for i in range(4):
#   turtle.forward(10 * k)
#   turtle.right(90)

# turtle.color("black")
# start = -40
# end = 20

# turtle.penup()
# for x in range(start, end):
#   for y in range(start, end):
#     turtle.goto(x * k,y * k)
#     turtle.dot(3)


# turtle.done()


# -----------------------------------------------------


# import turtle

# k = 40
# turtle.left(90)
# turtle.tracer(0)
# turtle.screensize(10000, 10000)
# turtle.color("red")

# turtle.right(45)

# for i in range(7):
#   turtle.forward(5*k)
#   turtle.right(45)
#   turtle.forward(10*k)
#   turtle.right(135)

# turtle.color("black")
# start = -30
# end = 20

# turtle.penup()
# for x in range(start, end):
#   for y in range(start, end):
#     turtle.goto(x * k,y * k)
#     turtle.dot(3)


# turtle.done()

# -----------------------------------------------------


# import turtle

# k = 40
# turtle.left(90)
# turtle.tracer(0)
# turtle.screensize(10000, 10000)
# turtle.color("red")

# for i in range(5):
#   turtle.forward(9*k)
#   turtle.right(120)

# turtle.color("black")
# start = -30
# end = 20

# turtle.penup()
# for x in range(start, end):
#   for y in range(start, end):
#     turtle.goto(x * k,y * k)
#     turtle.dot(3)


# turtle.done()

# -----------------------------------------------------


# import turtle

# k = 40
# turtle.left(90)
# turtle.tracer(0)
# turtle.screensize(10000, 10000)
# turtle.color("red")

# for i in range(4):
#   turtle.forward(10*k)
#   turtle.right(60)
#   turtle.forward(10*k)
#   turtle.right(120)

# turtle.color("black")
# start = -30
# end = 20

# turtle.penup()
# for x in range(start, end):
#   for y in range(start, end):
#     turtle.goto(x * k,y * k)
#     turtle.dot(3)


# turtle.done()

# -----------------------------------------------------


import turtle
import random

k = 40
turtle.left(90)
turtle.tracer(0)
turtle.screensize(10000, 10000)
turtle.color("red")

colors = ["red", "green", "blue", "yellow", "purple"]

width = 20
i = 0

for i in range(4):
  width -= 2
  turtle.width(width)
  turtle.color(colors[i%5])
  for i in range(4):
    turtle.forward(6*k) 
    turtle.right(90)
    # width -= 1
    # turtle.width(width)
    # turtle.color(colors[i%5])
  width -= 2
  turtle.width(width)
  turtle.color(colors[i%5])
  turtle.forward(10*k)
  turtle.right(90)
  turtle.forward(3*k)

turtle.color("black")
start = -30
end = 20

turtle.penup()
for x in range(start, end):
  for y in range(start, end):
    turtle.goto(x * k,y * k)
    turtle.dot(3)


turtle.done()
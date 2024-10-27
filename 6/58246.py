import turtle

k = 40
turtle.left(90)
turtle.tracer(0)
turtle.screensize(10000, 10000)

turtle.color("red")


turtle.right(180)
turtle.forward(2 * k)
turtle.right(90)
turtle.forward(40 * k)
turtle.right(90)
turtle.forward(2 * k)
for i in range(4):
  turtle.setheading(90)
  turtle.circle(-5 * k, 180)

# ----
turtle.color("black")
start = -60
end = 20

turtle.penup()
for x in range(start, end):
  for y in range(start, end):
    turtle.goto(x * k,y * k)
    turtle.dot(3)

turtle.done()
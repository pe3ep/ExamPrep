import turtle

k = 50
turtle.left(90)
turtle.tracer(0)
turtle.screensize(10000, 10000)


turtle.color("red")
for i in range(4):
  turtle.forward(7*k)
  turtle.right(90)
  turtle.forward(7*k)
  turtle.left(90)
  turtle.forward(7*k)
  turtle.right(90)

turtle.color("black")
start = -20
end = 20

turtle.penup()
for x in range(start, end):
  for y in range(start, end):
    turtle.goto(x * k,y * k)
    turtle.dot(3)

turtle.done()
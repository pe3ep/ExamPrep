import turtle

turtle.color("red")
k = 50
turtle.tracer(0)
turtle.left(90)
turtle.screensize(3000, 3000)

for i in range(8):
  turtle.right(45)
  turtle.forward(6 * k)

turtle.penup()

turtle.color("black")
start = -10
end = 15

for x in range(start, end):
  for y in range(start, end):
    turtle.goto(x * k, y * k)
    turtle.dot(3)

turtle.done()
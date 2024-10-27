import turtle

k = 50
turtle.tracer(1, 0)
turtle.left(90)
turtle.screensize(3000, 3000)

for i in range(7):
  turtle.forward(10 * k)
  turtle.right(120)

turtle.penup()

start = -5
end = 15

for x in range(start, end):
  for y in range(start, end):
    turtle.goto(x * k, y * k)
    turtle.dot(3)

turtle.done()
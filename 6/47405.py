import turtle

k = 50
turtle.left(90)
turtle.tracer(0)
turtle.screensize(10000, 10000)
for i in range(4):
  turtle.color("red")
  turtle.forward(9*k)
  turtle.right(90)

for i in range(3):
  turtle.color("blue")
  turtle.forward(9*k)
  turtle.right(120)

turtle.color("black")
start = -20
end = 20

turtle.penup()
for x in range(start, end):
  for y in range(start, end):
    turtle.goto(x * k,y * k)
    turtle.dot(3)


turtle.done()
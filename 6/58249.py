import turtle

k = 50
turtle.left(180)
turtle.tracer(0)
turtle.screensize(10000, 10000)

turtle.color("red")


for i in range(5):
  turtle.circle(-5 * k, 180)
  turtle.left(90)
  turtle.circle(-5 * k, 180)
  turtle.left(90)
  turtle.circle(-5 * k, 180)
  turtle.left(90)


# ----
turtle.color("black")
start = -20
end = 20

turtle.penup()
for x in range(start, end):
  for y in range(start, end):
    turtle.goto(x * k,y * k)
    turtle.dot(3)

turtle.done()
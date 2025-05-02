# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=5

from turtle import *

screensize(10**5, 10**5)
tracer(0)
left(90)

k = 20
color("red")

for i in range(9):
  fd(22*k)
  right(90)
  fd(6*k)
  right(90)

penup()

fd(k)
right(90)
fd(5*k)
left(90)

pendown()

for i in range(9):
  fd(53*k)
  right(90)
  fd(75*k)
  right(90)

penup()
color("black")
for x in range(-100, 100):
  for y in range(-100, 100):
    goto(x*k,y*k)
    dot(3)

done()

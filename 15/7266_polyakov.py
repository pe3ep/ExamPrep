def f(a,x,y):
  return (3*x + 2*y > 95) or (4 * x < 3 * y) or (x + 4*y < a)

maxa = 0
for a in range(500):
  for x in range(500):
    for y in range(500):
      if f(a,x,y) == False:
        maxa = max(maxa, a)
print(maxa)
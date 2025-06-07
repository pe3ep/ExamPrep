def f(a):
  for x in range(1000):
    for y in range(1000):
      if ((x >= 27) or (2 * x < 3 * y) or (a > (x + 2) * (y - 3))) == False:
        return False
  return True

for a in range(1000):
  if f(a):
    print(a)
    break
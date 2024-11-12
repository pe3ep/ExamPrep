def f(A: int):
  for x in range(-250, 250):
    for y in range(-250, 250):
      if ((( x < 10) <= (y > 40)) or not((y < A) <= (x > A))) == False:
        return False
  return True


for A in range(-500, 500):
  if f(A):
    print(A)
    break
def f(A: int):
  for x in range(500):
    for y in range(500):
      if ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9)) != True:
        return False
  return True

maxA = 0
for A in range(500):
  if f(A):
    print(A)
    maxA = max(maxA, A)
print(maxA)
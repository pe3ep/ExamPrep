def isSimple(n: int):
  for i in range(2, n):
    if (n % i == 0):
      return False
  return True


for i in range(31, 0, -1):
  total = i * 4 + (31 - i) * 3 + 1
  if isSimple(total): print(i)

print(isSimple(103))


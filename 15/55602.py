def f(A):
  for x in range(500):
    if (((x & 114 != 0) or (x & 94 != 0)) <= ((x & 73 == 0) <= (x & A != 0))) == False: return False
  return True

for A in range(500):
  if f(A):
    print(A)
    break
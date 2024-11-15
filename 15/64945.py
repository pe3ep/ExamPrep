def f(A):
  for x in range(50074):
    if ( (x & 21074 != 0) <= ( (x & 12369 == 0) <= (x & A != 0) ) ) == False: return False
  return True

for A in range(50074):
  if f(A):
    print(A)
    break

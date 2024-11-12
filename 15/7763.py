def f(a1, a2):
  for x in range(1,35):
    if ( ((5 <= x <= 30) == (14 <= x <= 23)) <= (not(a1 <= x <= a2)) ) == False:
      return False
  return True
  
maxA = 0
for a1 in range(1, 35):
  for a2 in range(a1, 35):
    if(f(a1,a2)):
      maxA = max(maxA, (a2 - a1) + 1)

print(maxA)

def f(a1, a2):
  for x in range(500):
    if ( (15 <= x <= 40) <= (((21 <= x <= 63) and (not(a1 <= x <= a2))) <= (not(15 <= x <= 40))) ) == False: return False
  return True

minLen = 500
for a1 in range(13, 65):
  for a2 in range(a1, 65):
    if f(a1,a2):
      minLen = min(minLen, a2 - a1)

print(minLen)

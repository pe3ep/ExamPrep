def f(a1, a2):
  for x in range(20, 120):
    if ( (not((47 <= x <= 92) <= ((24 <= x <= 77) or (82 <= x <= 116)))) <= (not(a1 <= x <= a2) <= (not(47 <= x <= 92))) ) == False: return False
  return True

minA = 10**6
listA = []
for a1 in range(20, 120):
  for a2 in range(a1, 120):
    if(f(a1,a2)):
      minA = min(minA, (a2 - a1 + 1))
      listA.append((a1,a2))

listA.sort(key=lambda x: x[1] - x[0])
  
print(listA[:10])
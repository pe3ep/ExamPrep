def find(i: int):
  d = []
  for n in range(2, int(i**0.5) + 1):
    if i % n == 0:
      if n not in d: 
        d.append(n)
      if i // n not in d: 
        d.append(i // n)
  if len(d) == 0:
    return 0
  return min(d) + max(d)    
  
c = 0
for i in range(452_022, 10**6):
  if n := find(i):
    if n % 7 == 3:
      c += 1
      print(i, n)
      if c == 5:
        break
def find(i: int):
  l = []
  for n in range(int(i**0.5), 0, -1):
    if i % n == 0:
      n1 = i // n 
      if n1 - n > 100:
        break
      l.append(n1 - n)
  return len(l) >= 3

for i in range(1_000_000, 2_000_001):
  if find(i):
    print(i)
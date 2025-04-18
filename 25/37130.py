l = list(range(17, 300_001, 10))

def find(i: int):
  for n in l:
    if i % n == 0:
      return n

c = 0
for i in range(600_000, 10**6):
  if n := find(i):
    c += 1
    print(i, n)
    if c == 5:
      break
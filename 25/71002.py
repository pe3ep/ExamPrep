c = 0
for i in range(800000, 1000000):
  for s in range(2, int(i**0.5) + 1):
    if (i % s == 0):
      m = (i / s) + s
      if m % 10 == 4:
        c += 1
        print(i, m)
      break
  if c == 5:
    break

  

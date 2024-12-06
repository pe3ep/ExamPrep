c = 0
for i in range(700000, 10**7):
  M = 0
  for n in range(2, int(i**0.5) + 1):
    if (i % n == 0):
      M = n + (i // n)
      break
  
  if (M % 10 == 4):
    c += 1
    print(i, " - ", M)
    if c == 5: break
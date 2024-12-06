
for i in range(35 * 10**6, 40 * 10**6 + 1):
  c = 2 if (i % 2 != 0) else 1
  for n in range(2, int(i**(1/2) + 1)):
    if (i % n == 0):
      if (n % 2 != 0):
        c += 1
      if ((i // n) % 2 != 0) and (n != (i // n)):
        c += 1
    if c > 5:
      break
  if c == 5:
    print(i)



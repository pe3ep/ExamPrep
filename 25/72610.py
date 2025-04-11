def M(N):
  nsum = []
  for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
      if i not in nsum:
        nsum.append(i)
      if (N // i) not in nsum:
        nsum.append(N // i)
  nsum = sorted(nsum, reverse=True)
  if len(nsum) >= 2:
    return nsum[0] + nsum[1]
  return 0
    

for N in range(112_500_000, 112_550_001):
  if M(N) % 10000 == 1214:
    print(N)

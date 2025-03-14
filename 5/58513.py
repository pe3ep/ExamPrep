maxN = 0
for N in range(10**6):
  binN = bin(N)[2:]
  if N % 5 == 0: 
    binN += "101"
  else:
    binN += "1"

  if int(binN, 2) % 7 == 0:
    binN += "111"
  else:
    binN += "1"

  R = int(binN, 2)
  # 1855663
  if R < 1855663:
    maxN = max(maxN, N)
print(maxN)
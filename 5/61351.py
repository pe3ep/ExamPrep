c = 0
for N in range(30 * 10**6, 46 * 10**6):
  binN = bin(N)[2:]
  m = bin(N % 3)[2:]
  binN += "0" * (2 - len(m)) + m
  j = bin(int(binN, 2) % 5)[2:]
  R = binN + "0" * (3 - len(j)) + j
  R = int(R, 2)

  if (1_111_111_110 <= R <= 1_444_444_416):
    c += 1

print(c)

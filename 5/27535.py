for n in range(2, 500):
  binN = bin(n)[2:]
  binN = binN + binN[1] + binN[0]
  if (int(binN, 2) > 90):
    print(n)
    break

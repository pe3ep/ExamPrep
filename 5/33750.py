for n in range(1000000, 2, -1):
  binN = bin(n)[2:]
  if (n % 5 == 0):
    binN += bin(5)[2:]
  else:
    binN += bin(1)[2:]

  if (int(binN, 2) % 7 == 0):
    binN += bin(7)[2:]
  else:
    binN += bin(1)[2:]

  if ((int(binN,2) < 1728404)):
    print(n)
    break



for n in range(2, 1000):
  binN = bin(n)[2:]

  if binN.count("1") % 2 == 0:
    binN = "10" + binN[2:] + "0"
  else:
    binN = "11" + binN[2:] + "1"
  
  r = int(binN, 2)

  if r > 50:
    print(n)
    break
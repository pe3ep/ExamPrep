for N in range(0,256):
  binN = bin(N)[2:]
  if len(binN) != 8:
    binN = "0" * (8 - len(binN)) + binN
  inversedN = ""
  for i in binN:
    if (i == "0"):
      inversedN += "1"
    else:
      inversedN += "0"
  
  R = int(inversedN, 2)
  R = R - N
  if (R == 111):
    print(N)

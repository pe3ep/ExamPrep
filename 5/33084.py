for N in range(1000):
  binN = bin(N)[2:]
  R = binN
  for i in range(2):
    R = R + str(R.count("1") % 2)
  R = int(R, 2)
  if R > 154:
    print(N)
    break
    

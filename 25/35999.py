for n in range(1, 40, 2):
  for m in range(0, 40, 2):
    N = 2**m * 3**n 
    if (200000000 < N < 400000000):
      print(N)

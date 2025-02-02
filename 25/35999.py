for n in range(1, 40, 2):
  for m in range(0, 40, 2):
    if (200000000 < 2**m * 3**n < 400000000): print(2**m * 3**n)

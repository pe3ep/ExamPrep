for n in range(100, 1000000):
  troika = []
  n = str(n)

  for i in range(len(n) - 2):
    troika.append(int(n[i:i+3]))
  
  if max(troika) - min(troika) == 623: print(n); break

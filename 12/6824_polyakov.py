for n in range(3, 10_001):
  s = "1" + "8"*n

  while s.count("18") or s.count("388") or s.count("888"):
    if s.count("18"):
      s = s.replace("18", "8", 1)
    if s.count("388"):
      s = s.replace("388", "81", 1)
    if s.count("888"):
      s = s.replace("888", "3", 1)
    
  if s.count("1") == 3:
    print(n)
    break
for n in range(3, 10000):
  s = "5" + ("2" * n)

  while s.count("72") or s.count("522") or s.count("2222"):
    if s.count("72"):
      s = s.replace("72", "2", 1)
    if s.count("522"):
      s = s.replace("522", "27", 1)
    if s.count("2222"):
      s = s.replace("2222", "5", 1)

  total = s.count("1") + s.count("2") * 2 + s.count("5") * 5 + s.count("7") * 7

  if total == 63:
    print(n)
    break


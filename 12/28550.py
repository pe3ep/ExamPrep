for i in range(1000):
  s = "1" * 10 + "2" * i

  while "21" in s:
    s = s.replace("21", "5", 1)

  total = s.count("1") + (s.count("2") * 2) + (s.count("5") * 5)
  if (total == 34):
    print(">>> ", i)
    # break


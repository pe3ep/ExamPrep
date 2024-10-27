rangeint = 50
for n1 in range(rangeint):
  for n2 in range(rangeint):
    for n3 in range(rangeint):
      s = "0" + "1" * n1 + "2" * n2 + "3" * n3

      while "01" in s or "02" in s or "03" in s:
        s = s.replace("01", "30", 1)
        s = s.replace("02", "101", 1)
        s = s.replace("03", "202", 1)

      if (s.count("1") == 15 and s.count("2") == 10 and s.count("3") == 60):
        print(">>> ", n1)
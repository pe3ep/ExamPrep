s = "2" + "9" * 100

while s.count("19") or s.count("299") or s.count("3999"):
  s = s.replace("19", "2", 1)
  s = s.replace("299", "3", 1)
  s = s.replace("3999", "1", 1)

print(s)
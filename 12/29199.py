s = "0" + "1" * 12 + "2" * 15 + "3" * 17

while s.count("01") or s.count("02") or s.count("03"):
  s = s.replace("01", "20", 1)
  s = s.replace("02", "120", 1)
  s = s.replace("03", "302", 1)

print(">>> ", s.count("1"))
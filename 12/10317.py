s = "8" * 125

while s.count("333") or s.count("888"):
  if s.count("333"):
    s = s.replace("333", "8", 1)
  else:
    s = s.replace("888", "3", 1)

print(">>> ", s)
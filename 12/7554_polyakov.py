# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1

s = "9" * 81
while s.count("33333") or s.count("999"):
  if s.count("33333"):
    s = s.replace("33333", "99", 1)
  else:
    s = s.replace("999", "3", 1)

print(s)
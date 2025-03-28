# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1

from itertools import product

c = 0
for i in product("01", repeat=11):
  if ("".join(i).count("1") + 8) % 5 != 0:
    c += 1

print(c)
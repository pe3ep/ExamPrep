from itertools import product

c = 0
for i in product("0123456789AB", repeat=5):
  if i.count("7") == 1 and i[0] != "0":
    n = 0
    for x in i:
      if int(x, 12) > 8:
        n += 1
    if n <= 3:
      c += 1

print(c)
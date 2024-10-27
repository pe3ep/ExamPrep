from itertools import product

c = 0
for i in product("10", repeat=13):
  i = "".join(i)

  if (12 + (i.count("1")) == 14):
    c += 1

print(">>> ", c)
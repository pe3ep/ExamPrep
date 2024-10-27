from itertools import product

c = 0
for i in product("10", repeat=11):
  i = "".join(i)

  if (8 + i.count("1")) % 5 != 0:
    print(i)
    c += 1

print(">>> ", c)
from itertools import *

c = 0
for i in product("КОНФЕТА", repeat=5):
  if i.count("Е") == 2 and i[1] != "Ф":
    c += 1
    print(i)

print(c)
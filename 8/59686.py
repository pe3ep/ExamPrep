from itertools import *

words = list(product("ЕГЭ", repeat=5))
c = 0
for i in words:
  if ( i[0] != "Г" ):
    c += 1
    # break

print(c)
from itertools import *

p = list(product("ABCDEX", repeat=4))

c = 0
for i in p:

  i = "".join(i)
  if (i.count("X") == 1):
    if (i[0] == "X" or i[3] == "X"):
      # print("i: " + i)
      c += 1

print(c)
from itertools import *

c = 0
for i in permutations("ДЕМЬЯН"):
  if (i[0] != "Ь" and "".join(i).count("ЕЬ") == 0 and "".join(i).count("ЯЬ") == 0):
    c += 1

print(c)
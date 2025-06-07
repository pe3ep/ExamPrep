from itertools import *
c = 0
for i in product([0,1], repeat=14):
  if (10 + i.count(1)) % 2 == 0:
    c += 1

print(c)
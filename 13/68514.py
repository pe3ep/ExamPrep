# 14 x 1

from itertools import product

c = 0
for i in product([0,1], repeat=3):
  if (14 + i.count(1)) % 4 != 0:
    c += 1

print(c)

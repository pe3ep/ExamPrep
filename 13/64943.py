# 11001010.00000011.00010000.00000000
# 6x1

from itertools import product

c = 0
for i in product([0,1], repeat=12):
  if (i.count(1) + 6) % 2 == 0:
    c += 1

print(c)
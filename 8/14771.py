from itertools import *

words = list(product('АПРСУ', repeat=3))
c = 0
for i in words:
  c += 1
  if (i[0] == "Р"):
    print(c)
    break
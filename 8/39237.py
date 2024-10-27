from itertools import *

words = list(product('АВОРТ', repeat=4))
c = 0
correct = ("Т", "А", "Р", "А")
for i in words:
  c += 1
  if (i == correct):
    print(c)
    break
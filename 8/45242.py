from itertools import *



words = list(product('АБРТЫ', repeat=5))
c = 0
for i in words:
  c += 1
  i = i[0] + i[1] + i[2] + i[3] + i[4]
  if (i.count("Ы") == 0 and i.count("АА") == 0):
    print(c, i)
    exit()

  # for k in range(1,5):
  #   if (i[k] != "Ы" and i[k - 1] != "Ы") and (i[k] != "А" and i[k - 1] != "А"):
  #     print(i)
  #     exit()


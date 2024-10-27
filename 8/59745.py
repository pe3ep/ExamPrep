from itertools import product
sortedString = sorted("АЛГОРИТМ")

index = 0
c = 0
for i in product(sortedString, repeat=5):
  i = "".join(i)
  index += 1
  if (index % 2 != 0 and i[0] != "Г" and i.count("И") >= 2):
    # print("index: " + str(index))
    # print("i: " + str(i))
    c += 1
# 000000000000
print(c)
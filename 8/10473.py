from itertools import product
# 1234
# product
# count(1) = 2

c = 0
for i in product("1234", repeat=5):
  i = "".join(i)
  if (i.count("1") == 2): 
    c += 1;
print(c)
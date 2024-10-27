from itertools import *

# words = list(product("БКФЦ", repeat=5))
# c = 0
# for i in words:
#   c += 1
#   if (c == 486):
#     i = "".join(i)
#     print(i)
#     break

# c = 0
# for i in product("МАНГУСТ", repeat=6):
#   i = "".join(i)
#   if (i[0] != 'А' and i.count("У") != 0 and i.count("М") == 2):
#     print(i)
#     c += 1
# print(">>> ", c)

# c = 0
# for i in product(sorted("АИОУЭ"), repeat=4):
#   c += 1
#   i = "".join(i)
#   if (i == "ИААЭ"):
#     print(i)
#     print(">>> ", c)

# c = 0
# for i in product("БРОНХИ", repeat=4):
#   i = "".join(i)
#   if (i.count("Х") == 1):
#     c += 1
#     print(i)
# print(">>> ", c)

c = 0
for i in product("ABCDXYZ", repeat=4):
  i = "".join(i)
  if ((i[0] == "X" and i.count("X") == 1) or (i[0] == "Y" and i.count("Y") == 1) or (i[0] == "Z" and i.count("Z") == 1)):
    c += 1
    print(i)
print(">>> ", c)

# c = 0
# for i in product("ВИРТ", repeat=4):
#   c += 1
#   if (c == 249):
#     i = "".join(i)
#     print(i)
#     break
# # print(">>> ", c)

# def getNewN(N: str):
#   if len(N) == 11:
#     return 1

#   var = []
#   for i in "012345678":
#     n1 = int(N[-1])
#     n2 = int(i)

#     if (n1 + n2) % 2 == 0 and n2 > n1:
#       var.append(N + i)
#     elif (n1 + n2) % 2 != 0 and n2 < n1:
#       var.append(N + i)

#   return sum([getNewN(i) for i in var])


# k = 0
# for i in "12345678":
#   k += getNewN(i)
#   print(1)
# print(k)

# c = 0
# words = []
# for i in product(sorted("ПАРУС"), repeat=5):
#   i = "".join(i)
#   c += 1
#   if (i.count("У") == 1 and i.count("АА") == 0):
#     words.append(c)
    
# print(">>> ", words[-1])

# c = 0
# for i in product(sorted("УЧЕНИК"), repeat=5):
#   i = "".join(i)
#   if (i[0] == "У" and i[-1] == "К"):
#     c += 1
    
# print(">>> ", c)
    

from itertools import product

def check1(para: str):
  return (int(para[0]) < int(para[1]) and ((int(para[0]) % 2 == 0 and int(para[1]) % 2 == 0) or (int(para[0]) % 2 != 0 and int(para[1]) % 2 != 0)))
  
def check2(para: str):
  return (int(para[0]) > int(para[1]) and ((int(para[0]) % 2 != 0 or int(para[0]) % 2 == 0) or (int(para[0]) % 2 == 0 and int(para[1]) % 2 != 0)))

goodNumbers = []
badNumbers = []

for i in product("012345678", repeat=2):
  i = "".join(i)
  if (check1(i) or check2(i)):
    goodNumbers.append(i)
  else:
    badNumbers.append(i)

# print("Total badNumbers: ", len(badNumbers))
# print("Total goodNumbers: ", len(goodNumbers))
# print("Total productgoodNumbers: ", len(list(product(goodNumbers, repeat=6))))

c = 0
for bad in badNumbers:
  for bignum in product(goodNumbers, repeat=6):
    bignum = "".join(bignum)
    if (bignum.count(bad) == 0):
      c += 1

print(c)

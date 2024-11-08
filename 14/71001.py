def baseConvert(num: int, base: int):
  remainders = []
  while num != 0:
    remainders.append(num % base)
    num = num // base
  remainders.reverse()
  return remainders


for x in range(0, 2031):
  sum = 7**170 + 7**100 - x
  if (baseConvert(sum, 7).count(0) == 71):
    print(">>> ", x)
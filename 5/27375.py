def convert(num, base):
  remainders = []
  while (num > 0):
    remainders.append(num % base)
    num = num // base
  remainders.reverse()
  return remainders

def convertBack(array: list, base: int):
  array.reverse()
  base10 = 0
  for item in range(0, len(array)):
    base10 += array[item]*base**item
  return base10


for n in range(1, 1000):
  base3n = convert(n, 3)
  base3n.append(n % 3)
  print(convertBack(base3n, 3))

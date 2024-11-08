n = 3 * 343**8 + 5 * 49**12 + 7**15 - 49

def converter(num: int, base: int):
  remainders = []
  while num != 0:
    remainders.append(num % base)
    num = num // base
  remainders.reverse()
  return remainders


sevenN = converter(n, 7)

max = 0
maxNum = 0
for i in range(0, 7):
  if sevenN.count(i) > max:
    max = sevenN.count(i)
    maxNum = i

print(max)
print(maxNum)

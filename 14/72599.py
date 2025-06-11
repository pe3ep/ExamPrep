# C59xBA98F * E3x5DA9C6 % 36 == 0

def conv(l: list, base: int) -> int:
  l.reverse()
  xsum = 0
  for i in range(len(l)):
    xsum += l[i] * base**i
  return xsum

for x in range(37):
  if (conv([12, 5, 9, x, 11, 10, 9, 8, 15], 37) * conv([14, 3 , x, 5, 13, 10, 9, 12, 6], 37) % 36 == 0):
    print(conv([2, x, 1], 37)) 
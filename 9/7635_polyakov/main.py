f = open('9.csv')
s = list(map(lambda x: list(map(int, x.split(","))), f.readlines()))


def n1(l: list[int]):
  c = 0
  for i in l:
    if (l.count(i) != 3 and l.count(i) != 1):
      return False
    if (l.count(i) == 3):
      c += 1
  if c == 3:
    return True
  return False


def n2(l: list[int]):
  psum = 0
  nsum = 0
  for i in l:
    if l.count(i) == 1:
      nsum += i
    else:
      psum += i
  if psum**2 > nsum**2:
    return True
  return False


c = 0
for i in s:
  if n1(i) and n2(i): c += 1

print(c)

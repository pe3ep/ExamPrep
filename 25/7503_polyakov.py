# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6

def M(i: int):
  M = 0
  d = []
  for n in range(2, int(i**0.5) + 1):
    if i % n == 0:
      if n not in d:
        d.append(n)
      if i // n not in d:
        d.append(i // n)
  if len(d) != 0:
    M = min(d) + max(d)
  return M


c = 0
for i in range(1_000_000, 0, -1):
  m = M(i)
  if m % 100 == 18:
    c += 1
    print(i, m)
    if c == 5:
      break
    
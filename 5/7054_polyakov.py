# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=14
def convert(i, b):
  r = []
  if i == 0: return ["0"]
  while i > 0:
    r.append(str(i % b))
    i = i // b
  r.reverse()
  return r

for n in range(500):
  sixN = convert(n, 6)
  if n % 3 == 0:
    sixN = sixN + sixN[:2]
  else:
    sixN = sixN + convert((n % 3) * 10, 6)
  
  r = int("".join(sixN), 6)
  if r > 680:
    print(r)
    break
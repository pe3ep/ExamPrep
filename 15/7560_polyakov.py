# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1

def f(x,y,a):
  return ((x + y) <= 30) or (y <= (x + 2)) or (y >= a)

maxA = 0

def idk(a):
  for x in range(100):
    for y in range(100):
      if f(x,y,a) == False:
        return False
  return True

for a in range(100):
  if idk(a):
    maxA = max(maxA, a)
  
print(maxA)
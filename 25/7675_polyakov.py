# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1
from fnmatch import *

for i in range(0, 10**10 + 1, 1917):
  if fnmatch(str(i), "3?12?14*5") and i % 1917 == 0:
    print(i, i // 1917)

# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1

import sys
sys.setrecursionlimit(10**6)
def f(n):
  if n == 1: return 1
  if n > 1: return (n - 1) * f(n - 1)

print((f(2024) + 2 * f(2023))/f(2022))
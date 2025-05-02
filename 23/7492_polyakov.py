# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6

def f(n, end):
  if n == end: return 1
  if n < end: return 0
  
  return f(n - 1, end) + f(n - 2, end) + f(n % 3, end)


print(f(16, 11) * f(11, 6))
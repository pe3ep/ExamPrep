# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1

def f(start, end):
  if start == end: return 1
  if start < end: return 0

  return f(start - 2, end) + f(start // 2, end)

print(f(36, 16) * f(16, 2))

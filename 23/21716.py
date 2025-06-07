# https://kompege.ru/variant?kim=25095608

def f(start, end):
  if start == end: return 1
  if start > end: return 0
  if start == 56: return 0
  return f(start + 3, end) + f(start + 7, end) + f(start * 3, end)

print(f(12, 40)*f(40, 72)*f(72, 89))
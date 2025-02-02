def f(num: int, to: int):
  if num > to: return 0
  if num == 5 or num == 10: return 0
  if num == to: return 1


  return f(num + 1, to) + f(num * 2, to) + f(num + 3, to)

print(f(2, 14))
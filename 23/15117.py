def f(num: int, to: int):
  if num > to or num == 15: return 0
  if num == to: return 1

  return f(num + 1, to) + f(num + 2, to)

print(f(3, 9) * f(9, 20))
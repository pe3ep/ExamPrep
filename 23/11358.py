def f(num: int, to: int):
  if num > to: return 0
  if num == to: return 1

  return f(num + 1, to) + f(num + 2, to) + f(num * 2, to)

print(f(3, 10) * f(10, 12))
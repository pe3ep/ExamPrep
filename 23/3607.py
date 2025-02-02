def f(num: int):
  if num > 50: return 0
  if num == 50: return 1

  return f(num + 2) + f(num * 5)

print(f(2))
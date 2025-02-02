# x - 2
# x // 2

def f(num, to):
  if num == to: return 1
  if num < to: return 0

  return f(num - 2, to) + f(num // 2, to)


print(f(38, 16) * f(16, 2))
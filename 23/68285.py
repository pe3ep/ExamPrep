def f(num: int, to: int):
  if num < to: return 0
  if num == 15 or num == 10: return 0
  if num == to: return 1

  S = 0
  if num % 2 == 0:
    S += f(num / 2, to)
  if num % 3 == 0:
    S += f(num / 3, to)
  return f(num - 1, to) + S

print(f(22, 1))
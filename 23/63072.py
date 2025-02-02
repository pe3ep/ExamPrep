def f(num: int, to: int, canSubtract: bool = True):
  if num - 1 > to: return 0
  if num == to: return 1
  
  if canSubtract == True:
    return f(num - 1, to, False) + f(num * 2, to) + f(num * 3, to)
  else:
    return f(num * 2, to) + f(num * 3, to)

print(f(3, 15))
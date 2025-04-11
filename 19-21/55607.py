def f(s1, s2, x):
  if s1 + s2 > 40 and (x == 4 or x == 2):
    return True
  elif s1 + s2 > 40 and x <= 3:
    return False
  elif x > 4:
    return False

  if x % 2 != 0:
    # Ваня
    if s1 > s2:
      return any([f(s1+i, s2, x + 1) for i in range(1, 4)] + [f(s1, s2*2, x + 1)])
    elif s1 < s2:
      return any([f(s1, s2+i, x + 1) for i in range(1, 4)] + [f(s1*2, s2, x + 1)])
    else:
      return any([f(s1, s2+i, x + 1) for i in range(1, 4)])
  else:
    # Петя
    if s1 > s2:
      return all([f(s1 + i, s2, x + 1) for i in range(1, 4)] + [f(s1, s2 * 2, x + 1)])
    elif s1 < s2:
      return all([f(s1, s2 + i, x + 1) for i in range(1, 4)] + [f(s1 * 2, s2, x + 1)])
    else:
      return all([f(s1, s2 + i, x + 1) for i in range(1, 4)])


answer = []
for s2 in range(1, 24):
  if f(17, s2, 0):
    answer.append(s2)

# print(min(answer), max(answer))
print(answer)

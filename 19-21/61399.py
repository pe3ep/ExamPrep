def f19(s: int, turn: int):
  if turn == 3 and s >= 84: return True
  if turn == 3 and s < 84: return False
  if turn < 3 and s >= 84: return False

  if turn % 2 != 0:
    # Петя
    return f19(s * (1.5 if s % 2 == 0 else 2), turn + 1) and f19(s + 1, turn + 1)
  else:
    # Ваня
    return f19(s * (1.5 if s % 2 == 0 else 2), turn + 1) or f19(s + 1, turn + 1)

def f20(s: int, turn: int):
  if turn == 4 and s >= 84: return True
  if turn == 4 and s < 84: return False
  if turn < 4 and s >= 84: return False

  if turn % 2 != 0:
    # Петя
    return f20(s * (1.5 if s % 2 == 0 else 2), turn + 1) or f20(s + 1, turn + 1)
  else:
    # Ваня
    return f20(s * (1.5 if s % 2 == 0 else 2), turn + 1) and f20(s + 1, turn + 1)

def f21(s: int, turn: int):
  if (turn == 5) and s < 84: return False
  if (turn == 3 or turn == 5) and s >= 84: return True
  if (turn < 5) and s >= 84: return False

  if turn % 2 != 0:
    # Петя
    return f21(s * (1.5 if s % 2 == 0 else 2), turn + 1) and f21(s + 1, turn + 1)
  else:
    # Ваня
    return f21(s * (1.5 if s % 2 == 0 else 2), turn + 1) or f21(s + 1, turn + 1)

for s in range(1, 84):
  if f21(s, 1) and (not f19(s, 1)):
    print(s)
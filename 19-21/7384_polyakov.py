# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6

def f20(turn, s, remain):
  if remain <= 0: return False
  if turn == 4 and s > 60: return True
  if turn < 4 and s > 60: return False
  if turn > 4: return False

  if turn % 2 != 0:
    # Петя
    return f20(turn + 1, s * 2, remain - s) or f20(turn + 1, s + 1, remain - 1)
  else:
    # Ваня
    return f20(turn + 1, s * 2, remain - s) and f20(turn + 1, s + 1, remain - 1)

def f21(turn, s, remain):
  # if remain <= 0: return False
  if turn in [3,5] and s > 60: return True
  if turn < 5 and s > 60: return False
  if turn > 5: return False

  if turn % 2 != 0:
    # Петя
    return f21(turn + 1, s + 1, remain - 1) if remain - s <= 0 else (f21(turn + 1, s * 2, remain - s) and f21(turn + 1, s + 1, remain - 1))
  else:
    # Ваня
    return f21(turn + 1, s + 1, remain - 1) if remain - s <= 0 else (f21(turn + 1, s * 2, remain - s) or f21(turn + 1, s + 1, remain - 1))
    


for s in range(1, 61):
  if f21(1, s, 80 - s):
    print(s)
def f20(currentS: int, currentTurn: int):
  # Петя
  if (currentS >= 31 and currentTurn == 4): return True
  if (currentS < 31 and currentTurn == 4): return False
  if (currentS >= 31 and currentTurn < 4): return False
  
  if currentTurn % 2 != 0:
    return f20(currentS + 1, currentTurn + 1) or f20(currentS * 3 - 2, currentTurn + 1)
  else:
    return f20(currentS + 1, currentTurn + 1) and f20(currentS * 3 - 2, currentTurn + 1)

def f21(currentS: int, currentTurn: int):
  # Петя
  if (currentS >= 31 and (currentTurn == 5 or currentTurn == 3)): return True
  if (currentS < 31 and currentTurn == 5): return False
  if (currentS >= 31 and currentTurn < 5): return False
  
  if currentTurn % 2 == 0:
    return f21(currentS + 1, currentTurn + 1) or f21(currentS * 3 - 2, currentTurn + 1)
  else:
    return f21(currentS + 1, currentTurn + 1) and f21(currentS * 3 - 2, currentTurn + 1)

for s in range(2, 31):
  if f20(s, 1):
    print("\033[96m20:", s)
  if f21(s, 1):
    print("\033[92m21:", s)

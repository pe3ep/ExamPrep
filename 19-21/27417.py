def f20(currentS1: int, currentS2: int, currentTurn: int):
  # true - Петя
  if (currentS1 + currentS2 >= 77 and currentTurn == 4): return True
  if (currentS1 + currentS2 < 77 and currentTurn == 4): return False
  if (currentS1 + currentS2 >= 77 and currentTurn < 4): return False
  
  # Петя
  if currentTurn % 2 != 0:
    return f20(currentS1 + 1, currentS2, currentTurn + 1) or f20(currentS1 * 2, currentS2, currentTurn + 1) or f20(currentS1, currentS2 + 1, currentTurn + 1) or f20(currentS1, currentS2 * 2, currentTurn + 1)
  # Ваня
  else:
    return f20(currentS1 + 1, currentS2, currentTurn + 1) and f20(currentS1 * 2, currentS2, currentTurn + 1) and f20(currentS1, currentS2 + 1, currentTurn + 1) and f20(currentS1, currentS2 * 2, currentTurn + 1)

def f21(currentS1: int, currentS2: int, currentTurn: int):
  # true - Ваня
  if (currentS1 + currentS2 >= 77 and (currentTurn == 5 or currentTurn == 3)): return True
  if (currentS1 + currentS2 < 77 and currentTurn == 5): return False
  if (currentS1 + currentS2 >= 77 and currentTurn < 5): return False
  
  # Петя
  if currentTurn % 2 != 0:
    return f21(currentS1 + 1, currentS2, currentTurn + 1) and f21(currentS1 * 2, currentS2, currentTurn + 1) and f21(currentS1, currentS2 + 1, currentTurn + 1) and f21(currentS1, currentS2 * 2, currentTurn + 1)
  # Ваня
  else:
    return f21(currentS1 + 1, currentS2, currentTurn + 1) or f21(currentS1 * 2, currentS2, currentTurn + 1) or f21(currentS1, currentS2 + 1, currentTurn + 1) or f21(currentS1, currentS2 * 2, currentTurn + 1)


for S in range(1, 70):
  if f20(S, 7, 1) == True:
    print("\033[96m20: ", S)
  
  if f21(S, 7, 1) == True:
    print("\033[92m21: ", S)
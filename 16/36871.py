def f(n: int):
  if n == 0: return 0

  if (n > 0) and (n % 2 == 0): return(f(n/2))

  if (n % 2 != 2): return(1 + f(n - 1))

counter = 0
for n in range(1, 1001):
  if (f(n) == 3): counter += 1

print(">>> ", counter)

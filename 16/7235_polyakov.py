import sys
sys.setrecursionlimit(10**6)
def f(n, x):
  if n >= 3000: return n
  if n < 3000: return n + 2 * x + f(n + 2, x)

for x in range(100):
  if f(28, x) - f(34, x) == 324:
    print(x)
    break
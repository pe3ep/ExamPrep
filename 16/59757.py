import sys
sys.setrecursionlimit(10**6)
def f(n: int):
  if (n < 11): return 10
  if (n >= 11): return(n + f(n - 1))

print(f(2024) - f(2022))
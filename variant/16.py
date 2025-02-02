# import sys
# sys.setrecursionlimit(10**6)

def f(n):
  if n == 0: return 1
  if n % 2 != 0: 
    print(n%10)
    return (n%10)*f(n//100)
  if n % 2 == 0: return f(n//100)

print("-> ", f(123456))
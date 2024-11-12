def DEL(n, m):
  return (n % m == 0)

def f(A):
  for x in range(1,500):
    if ( DEL(x, A) or ((70 <= x <= 90) <= (not(DEL(x, 27)))) ) == False:
      return False
  return True

for A in range(1, 500):
  if (f(A)):
    print(A)
def DEL(n, m):
  return (n % m == 0)

def f(A):
  for x in range(1, 500):
    if ( (not(DEL(x, A))) <= (DEL(x, 6) <= (not(DEL(x, 4)))) ) == False:
      return False
  return True

for A in range(1, 500):
  if (f(A)):
    print(A)
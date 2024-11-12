def TRIANGLE(n,m,k):
  # l = [n,m,k]
  # min1 = min(l)
  # l.remove(min1)
  # min2 = min(l)
  # l.remove(min2)

  # if ((min1 + min2) < l[0]): return True
  # return False

  return max(n,m,k) < m + n + k - max(n,m,k)


def f(A):
  for x in range(1, 500):
    if ( ((TRIANGLE(x,10,20) <= (not(max(x,8)) > 24))) == (not(TRIANGLE(3, A, x)))) == False: return False
  return True

for A in range(1,500):
  if (f(A)):
    print(A)
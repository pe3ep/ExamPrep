def get_prime(p):
  s = [2]
  for x in range(3, p):
    f = True
    for i in s:
      if x % i == 0:
        f = False
        break
    if f:
      s.append(x)
      yield x

for p in get_prime(90):
  for a in range(0, 27):
    N = 2**a * p**4
    if 45_000_000 <= N <= 50_000_000:
      print(N)
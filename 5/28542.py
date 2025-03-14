def convert(n: int, b: int):
  r = []
  if n == 0: return ["0"]
  while n > 0:
    r.append(str(n % b))
    n //= b
  r.reverse()
  return r

for N in range(1000):
  triN = convert(N, 3)
  triN.append(str(N % 3))
  R = int("".join(triN), 3)
  if R >= 1000:
    print(R)
    break
def blablal(n: int):
  N = str(n)
  ch = 0
  sumch = 0
  ne = 0
  sumne = 0
  for i in N:
    if int(i) % 2 == 0:
      ch += 1
      sumch += int(i)
    else:
      ne += 1
      sumne += int(i)
  if 0 in [ch, ne]:
    return False
  if ch > ne:
    return sumch
  return sumne

c = 0
for N in range(1000, 10000):
  blalba = blablal(N)
  if blalba == False:
    continue
  r = 0
  if blalba % 2 == 0:
    r = str(blalba) + max([n for n in str(N) if int(n) % 2 == 0])
  else:
    r = min([n for n in str(N) if int(n) % 2 != 0]) + str(blalba)
  if int(r) == 111:
    c += 1
print(c)
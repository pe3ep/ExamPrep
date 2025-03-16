f = open('18.csv')
s = f.readlines()

sums = []
promesh = float(s[0])
for i in range(1, len(s)):
  n1 = float(s[i - 1])
  n2 = float(s[i])

  if abs(n1 - n2) <= 8 and promesh >= 0:
    promesh += n2
  else:
    sums.append(promesh)
    promesh = n2

print(max(sums))


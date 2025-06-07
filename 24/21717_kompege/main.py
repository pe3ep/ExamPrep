f = open("24.txt")
s = f.readline()

l = s.split("RSQ")
miny = 10**10
for i in range(len(l) - 130):
  slice = l[i:i + 130]
  y = sum([len(i) for i in slice]) + 130 * 3
  for m in l[i + 130]:
    y += 1
    if m != "Q":
      break
  else:
    y += 1
  miny = min(miny, y)

print(miny)
        
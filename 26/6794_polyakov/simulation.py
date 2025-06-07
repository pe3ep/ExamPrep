f = open('26.txt')
n, k = map(int, f.readline().split())
m = [0] * (k + 1)
a = [[int(y) for y in x.split()] for x in f]
a.sort(key = lambda x:x[0])
count = 0
last = 0
for i in a:
  z = -1
  for j in range(1, k + 1):
    if m[j] <= i[0]:
      z = j
      break
  if z == -1:
    for j in range(1, k + 1):
      if m[j] < i[1] and (z == -1 or m[j] < m[z]):
        z = j
  if z != -1:
    count += 1
    last = z
    m[z] = i[1]
print(count, last)
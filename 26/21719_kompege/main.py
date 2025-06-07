f = open("26.txt")
f.readline()
s = list(map(lambda x: list(map(int, x.split())), f.readlines()))

students = {}
for id, num in s:
  if id in students:
    if num not in students[id]:
      students[id].append(num)
  else:
    students[id] = [num]

maxc = 0
minid = 10**6
for id in students:
  l = sorted(students[id])
  c = 1
  for i in range(len(l) - 1):
    n1 = l[i]
    n2 = l[i+1]
    if abs(n2 - n1) == 2:
      c += 1
    else:
      maxc = max(maxc, c)
      c = 1
    maxc = max(maxc, c)

  if maxc == c:
    minid = min(minid, id)

print(minid, maxc)
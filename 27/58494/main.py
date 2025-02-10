f = open("A.txt")
f.readline()
s = list(map(int, f.readlines()))

#! ----------- A -----------

c = 0
for a1 in range(len(s) - 1):
  for a2 in range(a1 + 1, len(s)):
    n1 = s[a1]
    n2 = s[a2]

    if ((a2 - a1) % 9) == ((n1 + n2) % 9):
      c += 1

print(c)

#! ----------- A -----------

f = open("B.txt")
f.readline()

mat = [[0] * 9 for i in range(9)]
k = 0
for i, x in enumerate(f.readlines()):
  x = int(x)
  for x1 in range(9):
    for i1 in range(9):
      if (x1 + x) % 9 == abs(i1 - i) % 9:
        k += mat[x1][i1]
  mat[x % 9][i % 9] += 1
print(k)



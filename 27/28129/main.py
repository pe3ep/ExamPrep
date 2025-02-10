f = open("B.txt")
f.readline()
s = list(map(int, f.readlines()))

d = 160
p = 7
x = (0, 0)

for a1 in range(len(s) - 2):
  for a2 in range(a1 + 1, len(s)):
    if (s[a1] % d != s[a2] % d) and (s[a1] % p == 0 or s[a2] % p == 0):
      if sum(x) < s[a1] + s[a2]:
        x = (s[a1], s[a2])

print(x)

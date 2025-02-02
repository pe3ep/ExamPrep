f = open("17.txt")
s = list(map(int, f.readlines()))

kratnoye = 0
for i in sorted(s):
  if i % 21 == 0:
    kratnoye = i
    break

maxsum = 0
c = 0
for i in range(len(s) - 1):
  if s[i] % kratnoye == 0 or s[i+1] % kratnoye == 0:
    maxsum = max(maxsum, s[i] + s[i+1])
    c += 1

print("c: ", c)
print("max: ", maxsum)
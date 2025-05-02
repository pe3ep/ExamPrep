import string
f = open("36879.txt")
s = f.readlines()
l = []
for i in s:
  if i.count("G") < 25:
    maxn = 0
    for a in string.ascii_uppercase:
      maxn = max(maxn, i.rfind(a) - i.find(a))
    l.append(maxn)

print(max(l))

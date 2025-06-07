s = open("24.txt").readline()

d = []
c = 0
for i in s:
  if c == 0 and i == "0":
    continue
  if i not in "01234567890ABCDEF":
    d.append(c)
    c = 0
    continue
  c += 1

print(max(d))  

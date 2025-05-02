f = open("26.txt")
f.readline()
s = list(map(lambda x: list(map(int, x.split())), f.readlines()))

s.sort(key=lambda x: [-sum(x[1:4]), -x[-1], x[0]])
# print(s[475], sum(s[475][1:4]))
print(len(list(filter(lambda x: sum(x[1:4]) == 154, s))))
good = s[:485]
for i in good:
  print(i, sum(i[1:4]))
print("-"*12)
for i in s[485:505]:
  print(i, sum(i[1:4]))
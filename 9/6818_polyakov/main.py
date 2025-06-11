f = open("9.csv")
s = list(map(lambda x: list(map(int, x.split(","))), f.readlines()))

c = 0
for i in s:
  repeat = [0 for i in range(7)]
  for n in i:
    repeat[i.count(n) - 1] += 1
    # if i.count(n) == 2 and n not in repeat:
    #   repeat.append(n)
  if (repeat[0] == 3 and repeat[1] == 4) and i.count(max(i)) == 1:
    print(sum(i))
    break
# print(s[:10]) 
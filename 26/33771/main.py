f = open("E:/EGE/26/33771/33771.txt")
S = list(map(int, f.readline().split(" ")))
budget = S[1]

A = []
B = []

for i in f.readlines():
  l = i.split(" ")
  if l[2] == "A":
    A.append( (int(l[0]), int(l[1])) )
  else:
    B.append( (int(l[0]), int(l[1])) )

B.sort(key=lambda x: x[0])
for price, volume in B:
  if price * volume <= budget:
    budget -= price * volume

A.sort(key=lambda x: x[0])
countA = 0
for price, volume in A: 
  for i in range(volume):
    if (price <= budget):
      budget -= price
      countA += 1

print("A ", countA, " remaining budget: ", budget)
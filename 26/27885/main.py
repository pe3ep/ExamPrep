f= open("27885.txt")
limit, users = list(map(int, f.readline().split(" ")))
s = sorted(map(int, f.readlines()))

summa = []
for i in s:
  if sum(summa + [i]) <= limit:
    summa.append(i)

summa.pop()
for i in range(len(s) - 1, -1, -1):
  n = s[i]
  if (sum(summa + [n]) <= limit):
    summa.append(n)

print("len ", len(summa))
print("max ", max(summa))
    
  

f = open('E:/EGE/26/27882/27882.txt')
S = list(map(int, f.readline().split(" ")))
data = sorted(list(map(int, f.readlines())))

summa = []
for i in data:
  if sum(summa) + i <= S[0]:
    summa.append(i)


newK = summa[-1] + (S[0] - (sum(summa)))
summa.pop()
summa.append(max(filter(lambda x: x <= newK, data)))
print("len ", len(summa), ", max ", max(summa), ", sum ", sum(summa))
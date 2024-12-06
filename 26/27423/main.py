f = open('E:/EGE/26/27423/27423.txt')
S, N = list(map(int, f.readline().split(" ")))
s = list(map(int, f.readlines()))

summ = 0
maxI = 0
c = 0
s = sorted(s)
for i in s:
  if (summ + i <= 8200):
    c += 1
    summ += i
    maxI = i
  # break

x = -1
while True:
  if s[x] <= abs((summ - maxI) - 8200):
    print(s[x])
    break
  x -= 1

print(c)

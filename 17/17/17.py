f = open("17.txt")
s = f.readlines()

maxnum = 0
for i in s:
  if int(i) % 1000 == 538:
    maxnum = max(maxnum, int(i))

c = 0
maxsum = 0
for i in range(len(s) - 3):
  n1 = int(s[i])
  n2 = int(s[i + 1])
  n3 = int(s[i + 2])
  n4 = int(s[i + 3])

  nums = [n1,n2,n3,n4]
  pat = 0
  tri = 0
  sem = 0
  for x in nums:
    if len(str(x)) == 5:
      pat += 1
    if x % 3 == 0:
      tri += 1
    if x % 7 == 0:
      sem += 1
  
  if pat >= 2 and pat != 4:
    if tri > sem:
      if sum(nums) >= maxnum and sum(nums) <= 2*maxnum:
        c += 1
        maxsum = max(maxsum, sum(nums))

print(c)
print(maxsum)
    

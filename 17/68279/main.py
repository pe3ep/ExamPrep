with open("E:/EGE/17/68279/17.txt") as xfile: strings = xfile.readlines()

nums = list(map(lambda x: int(x), strings))

maxInt = 0
for i in nums:
  if i % 1000 == 562:
    maxInt = max(maxInt, i)

def fiveznachnoye(args: list):
  da = 0
  net = 0
  for i in args:
    if 9999 < i < 100000:
      da += 1
    else:
      net += 1
  
  if da >= 1 and net >= 2: return True
  return False

def kratniye(args: list):
  tri = 0
  semb = 0
  for i in args:
    if i % 3 == 0: tri += 1
    if i % 7 == 0: semb += 1
  
  if semb > tri: return True
  return False


c = 0
maxSum = 0
for i in range(0, len(nums) - 3):
  n1 = nums[i]
  n2 = nums[i + 1]
  n3 = nums[i + 2]
  n4 = nums[i + 3]

  summa = n1 + n2 + n3 + n4
  if (summa > maxInt) and (summa < (maxInt * 2)) and fiveznachnoye([n1,n2,n3,n4]) and kratniye([n1,n2,n3,n4]):
    c += 1
    maxSum = max(maxSum, summa)

print("c: ", c)
print("maxSum: ", maxSum)



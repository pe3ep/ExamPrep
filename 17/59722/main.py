with open("E:/EGE/17/59722/1_17.txt") as xfile: strings = xfile.readlines()

nums = list(map(lambda x: int(x), strings))

def check(args: list):
  c = 0
  for i in args:
    if 99 < abs(i) < 1000:
      c += 1
  
  if (c == 1):
    return True
  return False

maxInt = -10000
for i in nums:
  if abs(i) % 100 == 17:
    maxInt = max(maxInt, i)
print(maxInt)
counter = 0
for i in range(0, len(nums) - 2):
  n1 = nums[i]
  n2 = nums[i + 1]
  n3 = nums[i + 2]

  if check([n1,n2,n3]):
    sum = n1 + n2 + n3
    print(n1,n2,n3)
    if sum < maxInt:
      counter += 1
  
print(">>> ", counter)

# count = 0
# f = open('E:/EGE/17/59722/1_17.txt')
# l = [int(i) for i in f]
# max_dvy = 0
# for i in range(len(l)):
#   if abs(l[i]) % 100 == 17:
#     max_dvy = max(max_dvy, l[i])
# for i in range(len(l) - 2):
#   c = 0
#   s = [l[i], l[i+1],  l[i+2]]
#   for x in s:
#     if 99 < abs(x) < 1000:
#       c += 1
#   if c == 1 and sum(s) < max_dvy:
#     count += 1
# print(count)
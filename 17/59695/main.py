with open('E:\\EGE\\17\\59695\\17.txt') as filee: strings = filee.readlines()
nums = list(map(lambda x: int(x), strings))

maxInt = max([i for i in nums if abs(i) % 100 == 15])

def poverka(n1,n2,n3): 
  c = 0
  for i in [n1,n2,n3]:
    if 999 < i < 10000: c += 1
  
  return (c == 1)


counter = 0
maxSum = 0
for i in range(0, len(nums) - 2):
  n1 = nums[i]
  n2 = nums[i + 1]
  n3 = nums[i + 2]

  if (poverka(n1,n2,n3) and (n1 + n2 + n3 >= maxInt)):
    counter += 1
    maxSum = max(maxSum, n1 + n2 + n3)

print("counter >>> ", counter)
print("maxSum >>> ", maxSum)

with open('E:\\EGE\\17\\48438\\17.txt') as filee: strings = filee.readlines()
nums = list(map(lambda x: int(x), strings))

minInt = min([i for i in nums if abs(i) % 10 == 7])

counter = 0
maxSum = 0
for i in range(0, len(nums) - 1):
  first = abs(nums[i])
  second = abs(nums[i + 1])

  if ((first % 10 == 7) != (second % 10 == 7)):
    if (first**2 + second**2 < minInt**2):
      counter += 1
      maxSum = max(maxSum, first**2 + second**2)
    
print("counter >>> ", counter)
print("maxSum >>> ", maxSum)

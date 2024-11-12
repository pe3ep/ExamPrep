with open("E:/EGE/17/70544/17.txt") as xfile: strings = xfile.readlines()

nums = list(map(lambda x: int(x), strings))

minInt = min(nums)


maxSum = 0
c = 0
for i in range(0, len(nums) - 1):
  n1 = nums[i]
  n2 = nums[i + 1]

  if (n1 % 16 == minInt) or (n2 % 16 == minInt):
    c += 1
    maxSum = max(maxSum, (n1 + n2))


print("maxSum : ", maxSum)
print("c : ", c)
with open("E:\\EGE\\17\\37336\\17.txt") as somelist: strings = somelist.readlines()
nums = list(map(lambda x: int(x), strings))
max_ = 0
counter = 0
for i in range(len(nums) - 1):
  if (nums[i] % 3 == 0 or nums[i + 1] % 3 == 0):
    counter += 1
    max_ = max(max_, nums[i + 1] + nums[i])
    
print("counter >>> ", counter, " >>> max ", max_)

  
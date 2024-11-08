with open('E:\\EGE\\17\\37356\\17.txt') as xlist: strings = xlist.readlines()
nums = list(map(lambda x: int(x), strings))

counter = 0
maxInt = 0
for x in range(len(nums) - 1):
  for y in range(x + 1, len(nums)):
    summa = nums[x] + nums[y]
    if summa % 9 == 0:
      counter += 1
      if (maxInt < summa): maxInt = summa
    
print("count >>> ", counter)
print("maxInt >>> ", maxInt)
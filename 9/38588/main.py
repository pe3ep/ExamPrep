with open("E:\\EGE\\9\\38588\\38588.txt", mode="r", encoding='utf-8-sig') as xfile: strings = xfile.readlines()
print(strings[:10])
c = 0
k = 0
for i in strings:
  k += 1
  try:
    nums = i.split(",")
    nums = sorted(map(int, nums))
    if (nums[0] + nums[1] > nums[2]):
      c += 1
  except:
    print(1, k)

print(c)

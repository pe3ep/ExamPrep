f = open("9.csv")
s = f.readlines()

def n1(nums: list[int]):
  for i in nums:
    if nums.count(i) == 4:
      return True
  return False


def n2(nums: list[int]):
  median = sum(nums) / len(nums)
  
  sortN = sorted(nums)
  repeatedNumbers = []
  for n in range(len(nums) - 1):
    if sortN[n] == sortN[n + 1]:
      repeatedNumbers.append(sortN[n])
  
  if (sum(repeatedNumbers) / len(repeatedNumbers)) < median:
    return True
  return False
   

c = 0
for i in s:
  i = list(map(int, i.split(",")))
  if n1(i) and n2(i):
    c += 1

print(c)


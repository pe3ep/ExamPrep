with open("E:\\EGE\\9\\63058\\63058.csv") as xfile: strings = xfile.readlines()

def e1(li: list[int]):
  for i in li:
    if li.count(i) > 1: return True
  return False

def e2(li: list[int]):
  return (li.count(max(li)) == 1)


def e3(li: list[int]):
  sum = 0
  for i in li:
    if li.count(i) > 1:
      sum += i

  return (sum < max(li))
  
c = 0
for i in strings:
  nums = list(map(int, i.split(",")))

  if e1(nums) and e2(nums) and e3(nums):
    c += 1

print(c)
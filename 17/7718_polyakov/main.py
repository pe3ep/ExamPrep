# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1

f = open('17.txt')
s = f.readlines()

maxE = 0
for i in s:
  n = int(i)
  if n % 10 == 3:
    maxE = max(maxE, n)

def n1(nums: list[int]):
  d2 = 0
  for i in nums:
    if i % 10 == 2:
      d2 += 1

  if d2 % 2 != 0 and max(nums) < maxE:
    return True
  return False


minSum = 10**10
c = 0
for i in range(len(s) - 3):
  nums = [int(s[i]), int(s[i+1]), int(s[i+2]), int(s[i+3])]
  if n1(nums):
    c += 1
    minSum = min(minSum, sum(nums))

print(minSum)
print(c)
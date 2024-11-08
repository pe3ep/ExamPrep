def base10convert(num: list, base: int):
  num.reverse()
  sum = 0
  counter = 0
  for i in num:
    sum += i * base**counter
    counter += 1
  return sum


for x in range(0, 31):
  sum = base10convert([1,2,3,x,10,11,3], 31) + base10convert([3, 12, 14, x, 3, 2, 1], 31)
  if (sum % 17 == 0):
    print(">>>, ", sum / 17)
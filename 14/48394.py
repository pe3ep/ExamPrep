def base10convert(num: list, base: int):
  num.reverse()
  sum = 0
  counter = 0
  for i in num:
    sum += i * base**counter
    counter += 1
  return sum


for x in range(0, 10):
  sum = base10convert([4, 12, x, 4], 15) + base10convert([x, 6, 2, 10], 13)

  if (sum % 121 == 0):
    print(sum / 121)
  

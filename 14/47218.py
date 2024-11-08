def base10convert(num: list, base: int):
  num.reverse()
  sum = 0
  counter = 0
  for i in num:
    sum += i * base**counter
    counter += 1
  return sum


for x in range(0, 15):
  sum = base10convert([1,2,3,x,5], 15) + base10convert([1,x,2,3,3], 15)

  if (sum % 14 == 0):
    print(">>> ", sum / 14)
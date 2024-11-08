def base10convert(num: list, base: int):
  num.reverse()
  sum = 0
  counter = 0
  for i in num:
    sum += i * base**counter
    counter += 1
  return sum


for x in range(8):
  for y in range(8):
    sum = base10convert([y,0,4,x,5], 11) + base10convert([2,5,3,x,y], 8)

    if (sum % 117 == 0):
      print(">>> ", sum / 117)

def base10convert(num: list, base: int):
  num.reverse()
  counter = 0
  sum = 0
  for i in num:
    sum += i * base**counter
    counter += 1
  return sum

# def baseConvert(num: int, base: int):
#   remainders = []
#   while num != 0:
#     remainders.append(num % base)
#     num = num // base
#   remainders.reverse()
#   return remainders

for x in range(0, 37):
  num1 = [1, 2, 3, x]
  num2 = [4, x, 5, 9]
  sum = base10convert(num1, 37) + base10convert(num2, 37)
  if (sum % 36 == 0):
    print(sum / 36)


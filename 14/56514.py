def base10convert(num: list, base: int):
  num.reverse()
  counter = 0
  sum = 0
  for i in num:
    sum += i * base**counter
    counter += 1
  return sum

for p in range(10, 50):
  for x in range(0, p):
    for y in range(0, p):
      if (base10convert([3,2,x,8], p) + base10convert([x,x,x,9], p) == base10convert([y,y,0,2], p)):
        print(">>> ", base10convert([y,y,x], p))
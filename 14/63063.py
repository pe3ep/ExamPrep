def base10convert(num: list, base: int):
  num.reverse()
  sum = 0
  counter = 0
  for i in num:
    sum += i * base**counter
    counter += 1
  return sum


for p in range(10, 39):
  for x in range(0, p):
    for y in range(0, p):
      if ((base10convert([5,8,x,7,2,3,y,4,9], 39) % 38 == 0) and (base10convert([y,x], 39)**(1/2) == int(base10convert([y,x], 39)**(1/2)))):
        print(">>> ", base10convert([y,x], 39))
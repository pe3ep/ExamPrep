def base10convert(num: list, base: int):
  num.reverse()
  sum = 0
  counter = 0
  for i in num:
    sum += i * base**counter
    counter += 1
  return sum


for p in range(7,37):
  for x in range(0, p):
    for y in range(0, p):
      for z in range(0, p):
        if (base10convert([y, 4, y], p) + base10convert([y, 6, 5], p) == base10convert([x, z, 2, 3], p)):
          print(">>> ", base10convert([x, y, z], p))
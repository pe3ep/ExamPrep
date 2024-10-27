num1 = 174457
num2 = 174505

for i in range(num1, num2 + 1):
  delitel = []  

  if i**0.5 == int(i**0.5): continue

  for n in range(2, int(i**0.5)):
    if (i % n == 0):
      delitel.append(n)
      delitel.append(i // n)
    if len(delitel) > 2: break
  
  if len(delitel) == 2:
    print(delitel)
    
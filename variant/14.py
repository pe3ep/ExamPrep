minN = 10000

for x in "0123456789AB":
  for y in "0123456789AB":
    summa = int(f"{y}AA{x}", 12) + int(f"{x}02{y}", 14)
    if summa % 80 == 0:
      minN = min(minN, summa)

print(minN / 80)

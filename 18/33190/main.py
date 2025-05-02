f = open("33190.csv")
s = list(map(float, f.readlines()))

posl = 0
summa = s[0]
 
for i in range(1, len(s)):
  posl = max(posl, summa)
  if abs(s[i] - s[i-1]) <= 10 and summa > 0:
    summa += s[i]
  else:
    summa = s[i]
posl = max(posl, summa)

print(posl)
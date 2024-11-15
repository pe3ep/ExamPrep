def f(a1,a2):
  for x in range(500):
    if ( (not((18 <= x <= 80) <= ((13 <= x <= 31) or (48 <= x <= 114)))) <= (not(a1 <= x <= a2) <= (not(18 <= x <= 80))) ) == False: return False
  return True

minLen = 1000
listd = []
for a1 in range(11, 120):
  for a2 in range(a1, 120):
    if f(a1,a2):
      listd.append((a1, a2))
      minLen = min(minLen, (a2 - a1))

print(*sorted(listd, key=lambda x: x[1] - x[0])[:10], sep="\n")
print(minLen)
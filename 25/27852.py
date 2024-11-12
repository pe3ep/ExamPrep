deliteli = []
for i in range(185311, 185330 + 1):
  delitel = [1, i]
  for x in range(2, i // 2 + 1):
    if (i % x == 0): delitel.append(x)
    if len(delitel) > 4: break
  if len(delitel) == 4:
    deliteli.append(sorted(delitel))

print(">>> ", deliteli)

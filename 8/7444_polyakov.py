from itertools import permutations

c = 0
for i in permutations("012344567", 6):
  i = "".join(i)
  if i[0] == "0":
    continue
  if i.count("4") == 2 and i.count("44") == 0:
    # if all(["".join(i).count(f"4{x}4") == 1 for x in "01234"]):
    if all([int(x) >= 5 for x in i[i.index("4") + 1:i.rindex("4")]]):
      c += 0.5

print(c)
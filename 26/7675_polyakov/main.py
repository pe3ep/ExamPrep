# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1

f = open("26.txt")
f.readline()
s = f.readlines()

db={}
for i in s:
  mark,price,class_ = list(map(int, i.split()))
  if (mark, class_) in db:
    db[(mark, class_)] += price
    continue
  db[(mark, class_)] = price

narushiteli = sorted(db, key=lambda x: db[x], reverse=True)[:3]

print(narushiteli)
for i in narushiteli:
  print(f"price of {i}", db[i])
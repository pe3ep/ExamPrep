with open("E:\\EGE\\24\\33103\\24.txt") as sfile: 
  strings = sfile.readlines()

c = 0
for i in strings:
  if (i.count("A") > i.count("E")):
    c += 1

print(c)
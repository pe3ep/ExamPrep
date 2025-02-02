from fnmatch import fnmatch

for i in range(328212, 1000000001, 9117):
  if (fnmatch(str(i), "3*37*3?9")):
    print(i)
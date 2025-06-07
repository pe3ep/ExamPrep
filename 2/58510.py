def f1(w, x, y, z):
  return (w or (not(y))) <= (z == x)
  
def f2(w, x, y, z):
  return (w or (not(y))) == (x <= z)

print("w x y z")
for w in [0,1]:
  for x in [0,1]:
    for y in [0,1]:
      for z in [0,1]:
        k = 0
        if (f2(w,x,y,z) == False and x == 0):
          k = 1
        if (f1(w,x,y,z) == f2(w,x,y,z) == False and y == 0):
          k = 2
        print(w,x,y,z,f1(w,x,y,z),f2(w,x,y,z), k)
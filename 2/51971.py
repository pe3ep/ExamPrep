print("x,y,z,w")
for x in range(2):
  for y in range(2):
    for w in range(2):
      for z in range(2):
        func = (x == (not y)) <= ((z <= (not w)) and (w <= y))
        if func: print(x,y,z,w, func)
        
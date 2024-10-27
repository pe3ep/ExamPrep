print("x,y,z,w")
for x in range(2):
  for y in range(2):
    for w in range(2):
      for z in range(2):
        func1 = ((x or not(y)) <= (w==z))
        func2 = ((x or not(y)) == (w <= z))
        if (func1 == False or func2 == False): print(x,y,z,w, func1, func2)
        
        
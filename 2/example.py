for x in range(2):
  for y in range(2):
    for w in range(2):
      for z in range(2):
        if (((y<=x)*(z or w))<=((x*(not(w))) or (y == z))) == 0:
          print(x, y, z, w)
file = open("E:\\EGE\\9\\68242\\68242.csv")
strings = file.readlines()

strings = list(map(lambda x: list(map(int, x.split(","))), strings))
MAX_X = 6
MAX_Y = len(strings)

def getGrid(x,y): 
  grid = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      # if x == 0 or x == MAX_X or y == 0 or y == MAX_Y:
      if (0 <= (y + j) < MAX_Y) and (0 <= (x + i) < MAX_X):
        # continue
        grid.append(strings[y + j][x + i])

  return grid
  
c = 0
for y in range(MAX_Y):
  interesting = 0
  for x in range(MAX_X):
    grid = getGrid(x, y)
    origin = strings[y][x]

    if (max(grid) > origin) and (strings[y].count(origin) == 1):
      interesting += 1
  
  if (interesting >= 3) and (len(set(strings[y])) != len(strings[y]) ):
    c += 1

print(c)

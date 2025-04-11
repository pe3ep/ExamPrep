f = open("26.txt")
headers = list(map(int, f.readline().split()))
s = list(map(lambda x: list(map(int, x.split())), f.readlines()))

mat: list[list[int | bool]] = []

def checkin(checksOut: int):
  for line in mat:
    if all(line) == False:
      for i in range(len(line)):
        if line[i] == False:
          line[i] = checksOut
          return
  
  mat.append([checksOut] + [False] * (headers[0] - 1))

def clearMat(time: int):
  for line in mat:
    for i in range(len(line)):
      if line[i] + 1 <= time:
        line[i] = False
    

lastTraveller = []
for traveller in sorted(s, key=lambda x: x[0]):
  clearMat(traveller[0])
  checkin(traveller[1])
  lastTraveller = traveller

clearMat(lastTraveller[0] + 1)

c = 0
for line in mat:
  for i in line:
    if i != False:
      c += 1

print(len(mat), c)
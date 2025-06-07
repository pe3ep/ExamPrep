f = open("B.txt")
f.readline()
s = list(map(lambda x: list(map(float, x.split())), f.readlines()))

first_cluster = []
second_cluster = []
third_cluster = []

for x, y in s:
  if y > 0 and x < -6:
    first_cluster.append((x, y))
  elif y > 0 and x >= -6:
    second_cluster.append((x, y))
  elif y < 0:
    third_cluster.append((x, y))

def find_centroid(cluster: list[list[float]]) -> list[float]:
  mind = 10**10
  point = []
  for x1, y1 in cluster:
    dsum = 0
    for x2, y2 in cluster:
      d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
      dsum += d
    mind = min(mind, dsum)
    if mind == dsum:
      point = [x1, y1]
  return point

data = [find_centroid(first_cluster), find_centroid(second_cluster), find_centroid(third_cluster)]
xsum = 0
ysum = 0
for x, y in data:
  xsum += x
  ysum += y

SCALE = 10_000
print(abs(xsum * SCALE / len(data)), abs(ysum * SCALE / len(data)))

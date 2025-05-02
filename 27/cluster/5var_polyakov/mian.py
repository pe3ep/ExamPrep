f = open("B.txt")
s = f.readlines()

first_cluster = []
second_cluster = []
third_cluster = []

for i in s:
  x, y = list(map(float, i.replace(",", ".").split()))

  # 1
  # if y > 1:
  #   first_cluster.append((x, y))
  # else:
  #   second_cluster.append((x, y))

  # 2
  if x > 7:
    first_cluster.append((x, y))
  elif y > 0.2*x + 0.6:
    second_cluster.append((x, y))
  else:
    third_cluster.append((x, y))


def find_centroid(cluster):
  mind = 10**10
  median = 0
  for x1, y1 in cluster:
    sumd = 0
    for x2, y2 in cluster:
      sumd += ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    mind = min(mind, sumd)
    if mind == sumd:
      median = (x1, y1)
  
  return median


data = [find_centroid(first_cluster), find_centroid(second_cluster), find_centroid(third_cluster)]

xsum = 0
ysum = 0
for x, y in data:
  xsum += x
  ysum += y

SCALE = 10_000

P = (xsum * SCALE / len(data), ysum * SCALE / len(data))
print(P)
    
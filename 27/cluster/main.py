# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1

f = open("27-B.txt")
s = f.readlines()

first_cluster = []
second_cluster = []
# For B file only
third_cluster = []

def find_median(cluster):
  xsum = 0
  ysum = 0
  for x,y in cluster:
    xsum += x 
    ysum += y 
  median = (xsum / len(cluster),  ysum / len(cluster))
  return min(cluster, key=lambda point: ((median[0] - point[0])**2 + (median[1] - point[1])**2)**0.5)

for i in s:
  x, y = map(float, i.replace(",", ".").split())

  # Separator function
  # y = -x + 4

  #* Clusters in A
  # if y < (-x + 4):
  #   first_cluster.append((x,y))
  # else:
  #   second_cluster.append((x,y))

  #* Clusters in B
  if y < (-x + 6):
    first_cluster.append((x,y))
  elif y < (1.4 * x):
    second_cluster.append((x,y))
  else:
    third_cluster.append((x,y))

# Data A
# data = [find_median(first_cluster), find_median(second_cluster)]

# Data B
data = [find_median(first_cluster), find_median(second_cluster), find_median(third_cluster)]

xsum = 0
ysum = 0
for x,y in data:
  xsum += x 
  ysum += y 
median = (xsum * 10_000 / len(data),  ysum * 10_000 / len(data))

print(median)
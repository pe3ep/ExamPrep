f = open("A.txt")
s = f.readlines()

first_cluster = []
second_cluster = []

def find_centroid(cluster: list[tuple[float,float]]):
  medX = sum([i[0] for i in cluster]) / len(cluster)  
  medY = sum([i[1] for i in cluster]) / len(cluster)  
  return sorted(cluster, key=lambda a: ((a[0] - medX)**2 + (a[1] - medY)**2)**0.5)[0]

for i in s:
  x, y = list(map(float, i.replace(",", ".").split()))

  # First cluster
  # F(x) = -x + 2
  # F(x) = x + 6
  # F(x) = x - 6
  if (y < -x + 2) and (y < x + 6) and (y > x - 6):
    first_cluster.append((x, y))
  
  # Second cluster
  if (y > -x + 2) and (y > x - 6) and (y < x + 6):
    second_cluster.append((x, y))

centroid1 = find_centroid(first_cluster)
centroid2 = find_centroid(second_cluster)
px = (centroid1[0] + centroid2[0]) * 100_000 // 2
py = (centroid1[1] + centroid2[1]) * 100_000 // 2
print(px, py)
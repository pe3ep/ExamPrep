# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6

f = open("B.txt")
s = list(map(lambda x: list(map(float, x.replace(",", ".").split())), f.readlines()))


# --- A ---
# first_cluster = []
# second_cluster = []
# for x, y in s:
#   if y < 5 and x < 5:
#     first_cluster.append((x, y))
#   elif y > 5 and x > 5:
#     second_cluster.append((x, y))

# --- B ---
first_cluster = []
second_cluster = []
third_cluster = []

for x, y in s:
  if y > 5 and x < 5:
    first_cluster.append((x, y))
  elif 1 < y < 5 and x < 6:
    second_cluster.append((x, y))
  elif 2 < y < 7 and 7 < x < 11:
    third_cluster.append((x, y))


def find_distance(cl1, cl2) -> tuple[float, float]:
  dmin = 10**6
  dmax = 0
  for x1, y1 in cl1:
    for x2, y2 in cl2:
      d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

      dmin = min(dmin, d)
      dmax = max(dmax, d)
  return (dmin * 10_000, dmax * 10_000)

# A
# print(find_distance(first_cluster, second_cluster))

# B
dmin = 10**6
dmax = 0
min1, max1 = find_distance(first_cluster, second_cluster)
min2, max2 = find_distance(second_cluster, third_cluster)
min3, max3 = find_distance(first_cluster, third_cluster)

dmin = min(dmin, min1, min2, min3)
dmax = max(dmax, max1, max2, max3)

print(dmin, dmax)
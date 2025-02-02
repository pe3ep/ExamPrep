f = open('E:/EGE/26/33198/33198.txt')
S = list(map(int, f.readline().split(" ")))

items = sorted(list(map(int, f.readlines())))

def dsfghjsdf(gruzin: list, slot: int):
  ostatok = S[1] - sum(gruzin)
  popped = gruzin.pop(slot)
  searchfor = popped + ostatok
  return max(filter(lambda x: gruzin[slot] <= x <= searchfor, items))

items1 = []

gruz = list(filter(lambda i: 200 < i < 210, items))
items = [i for i in items if not(200 < i < 210)]

# for i in items:
#   if 200 < i < 210:
#     gruz.append(i)
#     items.remove(i)
#   else:
#     items1.append(i)

# items = items1
for i in items:
  if i + sum(gruz) <= S[1]:
    gruz.append(i)

print(sorted(gruz))
print("len: ", len(gruz), " sum: ", sum(gruz))
print(dsfghjsdf(gruz, -1) + sum(gruz), " ; ", sum(gruz))
print(dsfghjsdf(gruz, -2) + sum(gruz), " ; ", len(gruz), " ; ", sum(gruz))



# graph = {'А': 'БГЕ', 'Б': 'АВ', 'В': 'БДК', 'Г': 'АЕД', 'Д': 'ВКГ', 'Е': 'АГЖ', 'К': 'ВДИ', 'Ж': 'ЕИ', 'И': 'ЖК'}
# table = '----++---' + '-----++-+' + '----+-++-' + '-------++' + '+-+----+-' + '++----+--' + '-++--+---' + '--+++----' + '-+-+-----'
# for item in permutations(graph):
#   answer = ''
#   for x in item:
#     for y in item:
#       if y in graph[x]:
#         answer += "+"
#       else:
#         answer += "-"
#   if answer == table: print(item)


from itertools import *

def f(x,y,z,w):
  return (not(z) == y) <= ((w and not(x)) == (y and x))

for a1,a2,a3,a4,a5,a6 in product([0,1], repeat=6):
  tab = [(a1,1,1,1), (1,1,a2,a3), (a4,a5,0,a6)]
  if len(tab) == len(set(tab)):
    for p in permutations("xyzw"):
      if [f(**dict(zip(p,r))) for r in tab] == [0,0,0]:
        print(p)
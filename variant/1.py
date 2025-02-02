from itertools import *


graph = {"А": "БГВ", "Б": "АВ","В": "БАЕ","Е": "ВДЖ","Ж": "ЕД","Д": "ГЕЖ","Г": "АД"}
tab = "-----++" + "--++-+-" + '-+-+---' + '-++-+--' + '---+--+' + '++----+' + '+---++-'

for p in permutations(graph):
  o = ''
  for x in p:
    for y in p:
      if y in graph[x]:
        o += "+"
      else:
        o += "-"
  if o == tab: print(p)
from itertools import *

def f(x,w,y,z):
  return not(x <= w) or (y == z) or y

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
  tab = [(a1,1,a2,0), (a3,0,1,a4), (a5,a6,0,a7)]
  if len(tab) == len(set(tab)):
    for p in permutations("xwyz"):
      if [f(**dict(zip(p,r))) for r in tab] == [0,0,0]:
        print(p)
from itertools import *

def f(x,y,z,w):
  return (( x and w ) or (w and z) == ((z <= y) and (y <= x)))

for a1,a2 in product([0,1], repeat=2):
  tab = [(1,0,1,1), (1,0,a1,0), (1,0,a2,0)]
  if len(tab) == len(set(tab)):
    for p in permutations("xyzw"):
      if [f(**dict(zip(p,r))) for r in tab] == [1,1,1]:
        print(p)
        break

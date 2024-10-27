from itertools import *

def f(x,y,z,w):
  return (x and y and not(z)) == (y or z or not(w))

for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
  tab = [(1,1,a1,1), (a2,0,a3,0), (1,a4,a5,1)]
  if len(tab) == len(set(tab)):
    for p in permutations("xyzw"):
      if [f(**dict(zip(p,r))) for r in tab] == [1,1,1]:
        print(p)
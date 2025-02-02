P = [10,11,12,13,14,15]
Q = [10,11,12,13,14,15,16,17,18,19,20]
R = [5,6,7,8,9,10,11,12,13,14,15]

mina = 10000
for a1 in range(5, 21, 5):
  for a2 in range(a1 + 5, 21, 5):
    for x in range(0, 50):
      if ((a1 <= x <= a2) <= (x in P)) and ((x in Q) <= (x in R)):
        mina = min(mina, a2 - a1 )
        # print(a1, a2)
print(mina)
  


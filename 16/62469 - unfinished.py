import sys
sys.setrecursionlimit(10**6)


def f(n: int):
  if (n < 15): return n
  if (n >= 15):
    return f(n % 15) * f(n // 15)

# # counter = 0
# # for n in range(15, 3**40):
# #   if (f(n) == 7560): counter += 1

print(">>> ", f(538185))


# def d(multipliedX: int):
#   if (multipliedX > 7560):
#     return 0
#   if (multipliedX == 7560):
#     return 1

#   counter = 0
#   for x in range(2,15):
#     counter += d(multipliedX * x)
#   return counter

# counter = 0
# for x in range(1,15):
#   counter += d(x)
# print(">>> ", counter)
  
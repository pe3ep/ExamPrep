f = open("26.txt")
headers = list(map(int, f.readline().split()))
s = list(map(lambda x: list(map(int, x.split())), f.readlines()))
# print(s)

s.sort(key=lambda x: [x[1], x[0]])

# print(s[:10])
seats = {}
for ryad, mesto in s:
  if mesto not in seats:
    seats[mesto] = ryad

r_mesto = 0
r_ryad = 0
for mesto in range(1, headers[2]):
  if mesto in seats:
    ryad = seats[mesto]
    check_ryad = headers[1] if (mesto + 1) not in seats else seats[mesto + 1]
    if ryad < check_ryad:
      


#   pass
# print(list(seats.items())[-10:])
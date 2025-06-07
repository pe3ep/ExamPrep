f = open("26.txt")
headers = list(map(int, f.readline().split()))
s = list(map(lambda x: list(map(int, x.split())), f.readlines()))

s.sort(key=lambda x: x[0])
workers = {i: 0 for i in range(1, 501)}
# workers = {}
c = 0
a = 0
for i in range(1, 501):
  time_in, time_out = s[i]
  workers[i] = time_out
  c += 1
queue = []
for time_in, time_out in s:
  queue.append((time_in, time_out))
  for qtime_in, qtime_out in queue:
    if time_in > qtime_out:
      queue.remove((qtime_in, qtime_out))
  for qtime_in, qtime_out in queue:
    for worker in workers:
      if workers[worker] <= qtime_in:
        workers[worker] = qtime_out
        queue.remove((qtime_in, qtime_out))
        c += 1
        a = worker
        break

print("worker", a)
print("count", c)




# Check if there are people coming in at the same time
# d = [s[i+1][0] - s[i][0] for i in range(len(s) - 1)]
# print(d.count(0))
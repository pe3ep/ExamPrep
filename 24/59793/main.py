f = open("E:\\EGE\\24\\59793\\24.txt")
s = f.readline()

a = list(map(len, s.split("V")))

minI = 10000
for i in range(1, len(a) - 119):
  sumSubstr = sum(a[i:i+119])
  minI = min(minI, sumSubstr)

print(minI + 120)
f = input("IP: ")
for i in f.split("."):
  print(i, " -> ", bin(int(i))[2:])

print("lalala: ", 249 & 240)
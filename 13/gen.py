ip = input("IP: ")

ip = ip.split(".")
for i in ip:
  print(i, " >>> ", bin(int(i)))
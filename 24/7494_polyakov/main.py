s = [len(i) for i in open("24.txt").readline().split("DE")]
print(max([sum(s[i:i+242]) + 480 for i in range(len(s))]))
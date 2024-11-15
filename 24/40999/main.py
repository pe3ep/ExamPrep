with open("E:\\EGE\\24\\40999\\24.txt") as xfile: string = xfile.readline()

print(len(max([s for s in string.split("E") if s.count("A") >= 3], key=len)))

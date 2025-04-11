# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное количество идущих подряд символов, среди которых каждая из букв UVWXYZ встречается не более ста раз.

f = open("24.txt")
s = f.readline()

data = {"U": [], "V": [], "W": [], "X": [], "Y": [], "Z": []}
maxlen = 0
l = 0

for i in range(len(s)):
  if s[i] in "UVWXYZ":
    data[s[i]].append(i)
    if len(data[s[i]]) > 100:
      if data[s[i]][0] + 1 > l:
        l = data[s[i]][0] + 1
      data[s[i]].pop(0)
  maxlen = max(maxlen, i - l + 1)

print(maxlen)
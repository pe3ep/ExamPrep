# Текстовый файл 24-263.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита. Определите минимальную длину подстроки, в которой символ Z встречается не менее 120 раз. 
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=19

f = open('24.txt')
s = f.readline()

data = list(map(len, s.split("Z")))

minSum = 10**6
for i in range(1, len(data) - 120):
  minSum = min(minSum, sum(data[i:i+119]) + 120)

print(minSum)
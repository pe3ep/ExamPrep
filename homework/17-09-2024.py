
#* 6

# def findIntSum(num: int):
#   s = 0
#   while num > 0:
#     s += num % 10
#     num = num // 10
#   return s

# for n in range(1, 10000):
#   binN = bin(n)[2:]
#   for x in range(3):
#     append = 0
#     r = int(binN, 2)
#     sumR = findIntSum(r)
#     if (sumR % 2 != 0): append = 1
#     binN += str(append)
#   r = int(binN, 2)
#   if r > 2054: print(r); break 

#? Result: 2057

#* 7

# def findIntSum(num: int):
#   s = 0
#   while num > 0:
#     s += num % 10
#     num = num // 10
#   return s

# for n in range(1, 10000):
#   binN = bin(n)[2:]
#   for x in range(3):
#     append = 0
#     r = int(binN, 2)
#     sumR = findIntSum(r)
#     if (sumR % 2 != 0): append = 1
#     binN += str(append)
#   r = int(binN, 2)
#   if r > 1028: print(r); break 

#? Result: 1035

#* 8

# def baseConvert(num, base):
#   remainders = []
#   while (num > 0):
#     remainders.append(num % base)
#     num = num // base
#   remainders.reverse()
#   return remainders

# def convertBack(array: list, base: int):
#   array.reverse()
#   base10 = 0
#   for item in range(0, len(array)):
#     base10 += array[item]*base**item
#   return base10


# for n in range(1, 10000):
#   base3N = baseConvert(n, 3)
#   base3N.append(n % 3)
#   n = convertBack(base3N, 3)
#   if (n >= 1000): print(n); break

#? Result: 1003

# max = 0
# for n in range(1, 10000):
#   binN = bin(n)[2:]
#   append = '11'
#   if (n % 2 == 0): append = '00'
#   binN += append
#   r = int(binN, 2)
#   if r < 134:
#     max = n
#   else:
#     break
# print(max)

#* 10

# for n in range(1, 10000):
#   binN = bin(n)[2:]
#   if (n % 2 == 0): 
#     binN = "10" + binN
#   else:
#     binN = "1" + binN + "01"
  
#   r = int(binN, 2)
#   if (r > 441): print(n); break

#? Result: 47
  
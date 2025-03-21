# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1
from itertools import product

s = open("24.txt").readline()

valid_strings = []
buffer = ""

variants = list(product("+*", repeat=2))

def find_max(s: str):
  s = s.split("+")
  r = []
  for i in s:
    if eval(i) == 0:
      r.append(len(i))
    else:
      r.append(0)

  lens = []
  c = 0
  for i in range(len(r)):
    if r[i] == 0:
      lens.append(c - 1)
      c = 0
      continue
    c += r[i] + 1

  if len(lens) == 0:
    return c - 1
  return max(lens)    
  
# Find vaild strings
for i in range(1, len(s)):
  char_prev = s[i - 1]
  char = s[i]

  if (char_prev, char) not in variants:
    if buffer == "" and char_prev in "*+":
      continue
      
    buffer += char_prev
  elif buffer != "":
    valid_strings.append(buffer)
    buffer = ""

searchingIn = sorted(valid_strings, key=len, reverse=True)[:100]
maxLen = 0
for i in searchingIn:
  maxLen = max(maxLen, find_max(i))

print(maxLen)

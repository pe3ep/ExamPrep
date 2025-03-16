# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=1
from itertools import product

s = open("24.txt").readline()

valid_strings = []
buffer = ""

variants = list(product("+*", repeat=2))
maxLen = 0


def isCorrect(s, start, end):
  return s[start:end][0] not in "*+" and s[start:end][0] != "0" and s[start:end][-1] not in "+*"

def find_max(s: str):
  start = 0
  maxLen = 0
  while start != len(s):
    end = len(s)
    for i in range(end, start, -1):
      if isCorrect(s, start, i):
        part = s[start:i]
        if eval(part) == 0:
          maxLen = max(maxLen, len(part))
    start += 1
  return maxLen
  
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

  # for part in sorted(parts, key=len, reverse=True):
  #   if eval(part) == 0: 
  

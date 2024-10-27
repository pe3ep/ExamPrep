# иммиграция систем исчесления
def immigrirovat(num, base):
  remainders = []
  while (num > 0):
    remainders.append(num % base)
    num = num // base
  remainders.reverse()
  return remainders
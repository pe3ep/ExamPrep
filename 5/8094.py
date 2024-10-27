#* https://inf-ege.sdamgia.ru/problem?id=8094
for r in range(44, 1000):
  binaryR = bin(r)[2:]
  binaryN = bin(r)[2:-2]
  for _ in range(2):
    remainder = sum(map(int, list(binaryN))) % 2
    binaryN += str(remainder)
  if (binaryR == binaryN):
    print(r)
    break

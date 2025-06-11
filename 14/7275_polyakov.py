# zxyx8 + xy517 = wzx62
import string
l = f"0123456789{string.ascii_uppercase}"
for p in range(9, 33):
  for x in l[:p]:
    for y in l[:p]:
      for z in l[:p]:
        for w in l[:p]:
          if int(f"{z}{x}{y}{x}8", p) + int(f"{x}{y}517", p) == int(f"{w}{z}{x}62", p):
            print(int(f"{x}{y}{z}{w}", p))
            exit()

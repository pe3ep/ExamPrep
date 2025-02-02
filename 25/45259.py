for a in range(10):
  for b in range(10):
    if int(f"12345{a}7{b}8") % 23 == 0:
      print(int(f"12345{a}7{b}8"), int(f"12345{a}7{b}8") // 23)
for n in range(13):
    binN = bin(n)[2:]
    if n % 2 == 0:
        binN = "10" + binN
    else:
        binN = "1" + binN + "01"

    R = int(binN, 2)
    print(R)

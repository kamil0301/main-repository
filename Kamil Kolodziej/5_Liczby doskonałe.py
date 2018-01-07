# szukanie liczb doskonałych:
#suma dzielników daje tę lilczbę np. 6=1+2+3
L = 1
n = 1
while True:
    L += 2**n
    do = int(L / 2)
    while True:
        for i in range(3, do, 2):
            if L % i == 0:
                break
        else:
            print(L * (2 ** n))
            break

    n +=1
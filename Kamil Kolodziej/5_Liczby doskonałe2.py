#suma dzielników daje tę lilczbę np. 6=1+2+3
L = 1
n = 1
a = 0
while True:
    L += 2**n
    do = int(L / 2)
    while True:
        if L % 2 == 0:
            break
        for i in range(3, do, 2):
            if L % i == 0:
                a = 0
            else:
                a = 1

        if a == 1:
            print(L * (2 ** n))
            a = 0
            break

    n +=1
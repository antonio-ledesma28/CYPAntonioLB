I = 3
SP = 0
M = float(input("Escribe M: "))
if M>= 1:
    SP += 1
    print("Nùmero primo:",1)
    if M >= 2:
        SP += 1
        print("Nùmero primo:",2)
while (I<=M):
    BAND = True
    J = 3
    while J<(I // 2):
        if (I % J) == 0:
            BAND = False
        J += 2
    BAND = True
    print("Nùmero primo:",I)
    SP +=1
print("Entre 1 y M hay",SP, "NÙMEROS PRIMOS")

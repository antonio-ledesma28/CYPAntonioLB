MAY = -100000
MEN = 100000
N = int(input("Escribe N"))
for NUM in range (1,N+1,1):
    if NUM > MAY:
        MAY = NUM
    if NUM < MEN :
        MEN = NUM
print(MAY,MEN)

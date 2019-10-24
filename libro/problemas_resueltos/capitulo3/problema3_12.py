MASUE = 0
N= int(input("Escribe el valor de N: "))
for I in range (1,N+1,1):
    NUMEMP = int(input("Escribe NUMEMP: "))
    SUE = float(input("Escribe SUE: "))
    if SUE > MASUE :
        MASUE = SUE
        MANUM = NUMEMP
print("MANUM", MANUM, "MASUE", MASUE, )

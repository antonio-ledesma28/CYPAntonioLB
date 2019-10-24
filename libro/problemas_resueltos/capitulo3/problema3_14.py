AP1 = 0
AP2 = 0
AP3 = 0
AP4 = 0
AP5 = 0
RECAU = 0
P1 = float(input("Escribe P1: "))
P4 = float(input("Escribe P2: "))
P3 = float(input("Escribe P3: "))
P2 = float(input("Escribe P4: "))
P5 = float(input("Escribe P5: "))

CLAVE = int(input("Escribe la clave: "))
CANT = int(input("Escribe la cantidad: "))
while (CLAVE != -1) and (CANT != -1) :
    if CLAVE == 1 :
        PRE = P1*CANT
        AP1 = AP1 + CANT
    elif CLAVE == 2 :
        PRE = P2*CANT
        AP2 = AP2 + CANT
    elif CLAVE == 3 :
        PRE = P3*CANT
        AP3 = AP3 + CANT
    elif CLAVE == 4 :
        PRE = P4 *CANT
        AP4 = AP4 + CANT
    elif CLAVE == 5 :
        PRE = P5*CANT
        AP5 + CANT
    print("CLAVE ES:", CLAVE, "LA CANTIDAD ES:", CANT, "Y EL PRECIO ES:" , PRE,)
    CLAVE = int(input("Escribe la clave:"))
    CANT = int(input("Escribe la cantidad: "))
print("CANTIDAD DE BOLETOS TIPO1: ", AP1)
print("CANTIDAD DE BOLETOS TIPO2: ", AP2)
print("CANTIDAD DE BOLETOS TIPO3: ", AP3)
print("CANTIDAD DE BOLETOS TIPO4: ", AP4)
print("RECAUDACIÓN DEL ESTADO: ", RECAU,)



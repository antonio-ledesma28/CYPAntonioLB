ARSU = 0
ARNO = 0
MERSU = 5000
MES = 0
ARCE = 0
for i in range (1,13,1):
    print(f"Mes {i}:")
    RNO = int(input("Promedio de lluvias del mes Zona Norte: "))
    RCE = int(input("Promedio de lluvias del mes Zona Centro: "))
    RSU = int(input("Promedio de lluvias del mes Zona Sur: "))
    ARNO += RNO
    ARCE += RCE
    ARSU += RSU
    if RSU < MERSU:
        MERSU = RSU
        MES = i
PRORCE = ARCE / 12
print(f"Promedio region centro: {PRORCE}")
print (f" Mes con menos lluvia en region sur: {MES}")
print(f"Registro del mes menor lluvia es: {MERSU}")
if ARNO > ARCE :
    if ARNO> ARSU :
        print("La region con mayor lluvia en la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
elif ARCE > ARSU :
    print ("La region con mayores lluvias es la region centro")
else:
    print("La region con mayor lluvias en la region sur")
print("Fin del programa")



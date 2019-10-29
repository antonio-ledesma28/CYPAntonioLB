MAYPRO = 0
N= int(input("Escribe N: "))
if ( N<=100):
    for I in range(1,N+1,1):
        FABRICA = int(input("escribe la fàbrica: "))
        TOTANU =0
        for J in range (1,13,1):
            MES = (float(input("Escribe el mes: ")))
            TOTANU += MES
            if J==7 and MES>3000000:
                print("FABRICA ES:", FABRICA,)
        if TOTANU>MAYPRO:
            MAYPRO = TOTANU
            CLAVE = FABRICA
        print("PRODUCCION ANUAL FABRICA", FABRICA, ":$", TOTANU,)
print("ERROR EN NUMERO DE FABRICA")



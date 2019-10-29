TIPO1 = 0
TIPO2 = 0
TIPO3 = 0
TIPO4 = 0
TIPO5 = 0
MCTIPO2 = 0
N = int(input("Escribe el valor de N: "))
for I in range(1,N+1,1):
    J = 1
    TOTVIN = 0
    for J in range (1,5,1):
        V = float(input("Escribe el valor de V: "))
        TOTVIN += V
        if J == 1:
            TIPO1 += V
        elif J == 2:
            TIPO2 += V
            if V>MCTIPO2:
                MCTIPO2= V
                AÑO = I
        elif J== 3:
            TIPO3 += V
            if V== 0:
                print(f"El año es: {I}, No se produjo vino tipo 3")
        elif J == 4:
            TIPO4 += V
        elif J == 5:
            TIPO5 += V
    print(f"El total de litros producidos por año es: {TOTVIN}")
print(f"Total tipo1 es: {TIPO1}")
print(f"Total tipo2 es: {TIPO2}")
print(f"Total tipo3 es: {TIPO3}")
print(f"Total tipo4 es: {TIPO4}")
print(f"Total tipo5 es: {TIPO5}")
print(f"El año en que se produjo mayor cantidad de vino tipo2 es: {AÑO}, y litros: {MCTIPO2}")

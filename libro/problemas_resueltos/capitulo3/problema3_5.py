SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Escribe el número de datos a ingresasr: "))
for I in range (1,N+1, 1):
    NUM = (f"Escribe NUM")
    if NUM > 0:
        SUMPOS += NUM
        CUEPOS += 1
    else :
        SUMOTR += NUM
PROGEN = (SUMPOS + SUMOTR)/N
PROPOS = (SUMPOS/CUEPOS)
print("CUEPOS PROPOS Y PROGEN" ,CUEPOS,PROPOS,PROGEN)

SUMPAR= 0
SUMIMP = 0
CUEPAR = 0
for I in range (1,271,1):
    NUM = (int(input("Ingresa el nùmero; ")))
    if NUM != 0:
        if (-1**NUM)>0 :
            SUMPAR+= NUM
            CUEPAR+= 1
        else :
            SUMIMP+= NUM
PROPAR = SUMPAR / CUEPAR
print (f"PROPAR es {PROPAR} y SUMIMP ES {SUMIMP}")

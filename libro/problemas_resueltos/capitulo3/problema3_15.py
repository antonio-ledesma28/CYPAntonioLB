CL = 0
CUENTA = 0
TIPO = input("Escribe el tipo de llamada I: Internacional, N: Nacionol, ó, L: Local")
DUR = int(input("Escribe la duración de la llamada en minutos: "))
while (TIPO !='X') and (DUR != -1) :
    if TIPO == 'I' :
        if DUR<3 :
            COSTO = 7.59 + (DUR-3)*3.03
        else :
            COSTO = 7.59
    elif TIPO == 'L' :
        CL += 1
        if CL > 50 :
            COSTO = 0.60
        else: COSTO = 0
    elif TIPO == 'N' : 
        if DUR > 3 : 
            COSTO = 1.20 + (DUR-3)*0.48
        else :
            COSTO =1.20
    CUENTA += COSTO
    TIPO = input("Escribe el tipo de llamada I: Internacional, N: Nacionol, ó, L: Local")
    DUR = int(input("Escribe la duración de la llamada en minutos: "))
print(CUENTA)

NOM = 0
SUE=float(input("Escribe el sueldo del trabajador: "))
while(SUE != -1):
    if SUE < 1000:
        NSUE =SUE *1.15
    else :
        NSUE = SUE *1.12
    
    NOM += NSUE
    print(f" El nuevo sueldo es de: {NSUE}")
    SUE = (float(input("Escribe otro sueldo: ")))
print(f"Nómina es: {NOM}")

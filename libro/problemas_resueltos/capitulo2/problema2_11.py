CLAVE = int(input("Escribe la clave de tu zona geogr{afica: "))
NUMIN = int(input("Escribe el número en minutos de la duración de la llamada: "))
if CLAVE ==12 :
    COST = NUMIN*2
elif CLAVE == 15 :
    COST = NUMIN *2.2
elif CLAVE ==18:
    COST = NUMIN*4.5
elif CLAVE == 19:
    COST = NUMIN*3.5
elif 22<CLAVE<26:
    COST = NUMIN*6
else :
    CLAVE == 29
    COST = NUMIN*5
print(f"El costo total de tu llamada es de {COST}")

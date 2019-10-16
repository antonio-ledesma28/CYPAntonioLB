MAT = int(input("Escribe tu matrícula de alumno: "))
CARR = input("Escribe la carrera a la que perteneces (en mayúsculas y sin acento): ")
SEM = int(input("Escribe el número de semestre aprobado: "))
PROM = float(input("Escribe tu promedio: "))
if CARR == 'ECONOMIA' :
    if SEM >=6 and PROM >= 8.8 :
        print (f"Tu matrícula es {MAT}, tu carrera es {CARR} y tú fuiste ACEPTADO")
elif CARR == 'COMPUTACION' :
    if SEM >6 and PROM > 8.5 :
        print(f"Tu matrícula es {MAT} y tu carrera es {CARR}, FUISTE ACEPTADO")
elif CARR == 'ADMINISTRACION' or CARR == 'CONTABILIDAD':
    if SEM > 5 and PROM > 8.5 :
        print(f"Tu matrícula es {MAT} y tu carrera es {CARR}, FUISTE ACEPTADO.")

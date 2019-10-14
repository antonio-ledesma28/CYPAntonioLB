MAT = int(input("Escribe tu matrícula de alumno: "))
CARR = str(input("Escribe la carrera a la que perteneces (en mayúsculas): "))
SEM = int(input("Escribe el número de semestre aprobado: "))
PROM = float(input("Escribe tu promedio: "))
if CARR == ECONOMIA :
        if SEM >=6 and PROM >= 8.8 :
            print (f"Tu matrícula es {MAT}, tu carrera es {CARR} y tú fuiste ACEPTADO")

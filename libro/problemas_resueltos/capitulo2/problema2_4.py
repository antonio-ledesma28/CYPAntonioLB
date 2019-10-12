MAT = int(input("Escribe la matrícula del alumno: "))
CAL1 = float(input("Escribe la primer calificación: "))
CAL2 = float(input("Escribe la segunda calificación: "))
CAL3 = float(input("Escribe la tercer calificación: "))
CAL4 = float(input("Escribe la cuarta calificación: "))
CAL5 = float(input("Escribe la quinta calificación: "))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
if PRO>=6:
    print(f"La matrícula es {MAT}, el promedio es de {PRO}. El alumno APROBÓ")
else:
    print(f"La matrícula es {MAT}, el promedio es de {PRO}. El alumno NO APROBÓ")
print("FIN DEL PROGRAMA")


SUE = float(input("Escriba el sueldo básico del trabajador: "))
CATE = int(input("Escriba la categoría del trabajador del (opciones del 1 al 8): "))
HE = int(input("Escribe las horas extras trabajadas: "))
if CATE == 1 :
    PHE = 30 
elif CATE == 2 :
    PHE = 38
elif CATE == 3:
    PHE = 50
elif CATE == 4 :
    PHE = 70
else:
    PHE = 0
if HE >30:
    NSUE = SUE+30*PHE
else:
    NSUE = SUE + HE*PHE
print (f"Tu nuevo sueldo es de {NSUE}")

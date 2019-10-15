otra =  bool(int(input("Hay más alumnos(0 no. 1 si):")))
suma = 0.0
cont = 0
while(otra == True):
    cal = float(input("Calificación: "))
    cont+=1
    suma += cal
    otra = bool(int(input("Hay más alumnos(0 no. 1 si):")))
print("suma",suma)
print("Promedio: ",suma/cont)
print("Fin del programa")


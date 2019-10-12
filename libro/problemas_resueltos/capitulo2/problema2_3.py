A = float(input("Escribe el primer término de tu ecuación: "))
B = float(input("Escribe el segundo término de tu ecuación: "))
C = float(input("Escribe el tercer término de tu ecuación (que sea distinto al primero): "))
DIS = (B**2)-(4*A*C)
if DIS >= 0 :
    X1 = ((-B)+(DIS**.5))/(2*A)
    X2 = ((-B)-(DIS**.5))/(2*A)
    print(f"La ecuación tiene dos posibles soluciones, las cuales son: {X1} y {X2}")
print("Fin del programa")

CATE = int(input("Dame la categoría del empleado del 1 al 4: "))
SUE = float(input("Dame el sueldo del trabajador: "))
NSUE= 0
if CATE == 1:
    NSUE = SUE*1.15
elif CATE == 2:
    NSUE = SUE*1.10
elif CATE == 3:
    NSUE = SUE*1.08
elif CATE == 4:
    NSUE = SUE*1.07
print(f"La categoría es: {CATE}")
print(f"El nuevo sueldo es {NSUE}")


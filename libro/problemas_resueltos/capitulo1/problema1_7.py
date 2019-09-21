L1 = float(input("Escribe la medida del primer lado del triángulo:"))
L2 = float(input("Escribe la medida del segundo lado del triángulo:"))
L3 = float(input("Escribe la medida del tercer lado del triángulo:"))
S = (L1 + L2 + L3)/2
AREA = (S*(S-L1)*(S-L2)*(S-L3))**0.5
print(f"El área de un triángulo con lados {L1}, {L2} Y {L3} es: {AREA}")

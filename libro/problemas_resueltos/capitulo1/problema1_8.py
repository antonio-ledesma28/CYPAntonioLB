X1 = float(input("Escribe la primer coordenada en x:"))
Y1 = float(input("Escribe la primer coordenada en y:"))
X2 = float(input("Escribe la segunda coordenada en x:"))
Y2 = float(input("Escribe la segunda coordenada en y:"))
DIS = (((X1-X2))**2 + ((Y1-Y2))**2)**0.5
print(f"La distancia entre el punto ({X1},{Y1})  y  ({X2},{Y2})  es de: {DIS} unidades")

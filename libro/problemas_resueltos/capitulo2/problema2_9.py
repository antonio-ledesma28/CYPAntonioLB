prebas = float(input("Precio básico del producto"))
if prebas>500:
    imp = 20*0.30+(prebas-40)*0.50
elif prebas > 40:
    imp = 20*0.30+(prebas+40)*0.40
elif prebas > 20:
    imp = (prebas-20)*0.30
else:
    imp = 0
pretot= prebas+imp
print(f"El precio básico es de {prebas} y el precio total es de {pretot}")



TIPOENF = int(input("Nùmero de enfermedad: "))
EDAD = int(input("Edad del paciente: "))
DIAS = int(input("Nùmero de dìas que el paciente estuvo hospitalizado: "))
if TIPOENF == 1 :
    COSTOT = DIAS*25
elif TIPOENF == 2 :
    COSTOT = DIAS * 16 
elif TIPOENF == 3 :
    COSTOT = DIAS * 20 
elif TIPOENF == 4 :
    COSTOT = DIAS *32
if  22 >=EDAD>=14:
    COSTOT = COSTOT *1.10

print(f"El costo total es de {COSTOT}")


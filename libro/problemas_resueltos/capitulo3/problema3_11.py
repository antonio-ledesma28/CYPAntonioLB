CAN1= 0
CAN2= 0
CAN3= 0
CAN4= 0
VOTO = int(input("Escribe tu voto del 1 al 4"))
while (VOTO != 0):
    if VOTO == 1 :
        CAN1 +=1
    elif VOTO == 2:
        CAN2 += 1
    elif VOTO ==3 :
        CAN3 += 1
    elif VOTO == 4:
        CAN4 += 1
    print("EL VOTO ES {VOTO}")
SUMV = CAN1 + CAN2 + CAN3 + CAN4
POR1 = (CAN1/SUMV)*100
POR2 = (CAN2/SUMV)*100
POR3 = (CAN3/SUMV)*100
POR4 = (CAN4/SUMV)*100

print("VOTO CANDIDATO1:",CAN1, "PORCENTAJE:", POR1,)
print("VOTO CANDIDATO2:",CAN2, "PORCENTAJE:", POR2,)
print("VOTO CANDIDATO3:",CAN3, "PORCENTAJE:", POR3,)
print("VOTO CANDIDATO4:",CAN4, "PORCENTAJE:", POR4,)
print("CANDIDATOS VOTANTES", SUMV,)



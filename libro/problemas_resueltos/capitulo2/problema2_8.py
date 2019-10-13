COMPRA = float(input("Monto de la compra"))
if COMPRA<500:
    PAGAR == COMPRA
else:
    if COMPRA <= 1000:
        PAGAR = COMPRA-COMPRA*0.05
    else:
        if COMPRA <= 7000:
        PAGAR = COMPRA-COMPRA*0.11
        else:
            if COMPRA <= 15000:
                PAGAR = COMPRA-COMPRA*0.18
            else :
                PAGAR = COMPRA-COMPRA*0.25
print("El monto a pagar con el descuento aplicado es de {PAGAR}")


EDAD= int( input ("Dame tu edad:"))
INE = bool(int(input("Tienes INE (0 NO/ 1 SI)?:")))
if EDAD >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puede entrar al Bar")
else:
    print("Eres menor de edad")
    print("Puedes ir a jugar LOL")
print("Fin del programa")

def sumar (x , y):
    z= x + y
    return z

def restar (x, y):
    return x - y
def mi_print( texto ):
    print(f"Éste es mi print: {texto}")
def multiplica (valor, veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la función")
    else:
        print(valor*veces)
def comanda (mesa, comensa1, entrada, medio, fuerte, postre='Gelatina de Limón'):
    print(f"Mesa: {mesa}   comensa1: {comensa1}")
    print(f"\t Entrada : {entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte: {fuerte}")
    print(f"\t Postre: {postre}")
def comanda2 (**comida):
    llaves = comida.keys()
    for elem in llaves:
        print(argumentos[index])
def imprime_argumentos (*argumentos):
    for index in range (len(argumentos)):
        print(argumentos[index])
def main():
    a = 10
    b= 5
    c = sumar(a,b)
    print(f"La suma de {a} y {b} es {c}")
    c= restar(a,b)
    print(f"La resta de {a} y {b} es {c}")
    mi_print("HOLA!!!!")
    multiplica(10,3)
    multiplica (10,None)
    multiplica('hola',3)
    comanda(2,1,"Ensalada", "Sopa de rana", "Filete de pompi de sirena", "Flan")
    comanda("Ensalada", "Sopa de rana", "Filete de pompi de sirena", "Flan",2,1)
    comanda(entrada="Ensalada",medio= "Sopa de rana",fuerte= "Filete de pompi de sirena",postre= "Flan", mesa=2, comensa1=1)
    comanda(entrada="Ensalada",medio= "Sopa de rana",fuerte= "Filete de pompi de sirena", mesa=2, comensa1=1)
    imprime_argumentos ('Hola', True, 3.1416,1000,{'id':'sc01','nombre': 'Juan'})
    imprime_argumentos()
    comanda2(entrada="Ensalada",medio= "Sopa de rana",fuerte= "Filete de pompi de sirena",postre = "Strudel de manzana", bebida='coca light', mesa=2, comensa1=1)
if __name__=='__main__' : # ¿Se mandó a ejecutar(interpretar) este archivo?
    main()
    

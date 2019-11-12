archivo = open("números.txt", "rt")
print(dir(archivo))

números1= archivo.read()
print(números1)
print(números1.split('\n'))
lista_num= []
for linea in números1.split('\n'):
    for número in linea.split(','):
        lista_num.append(int(número))
print(lista_num)
lista_num.sort()
print(f"\n Lista ordenada: {lista_num} \n")

print(f"El mayor es : {{lista_num[-1]} y el menor es: {lista_num[0]}")
archivo.close()

archivo=open("números.txt", "rt")
números2 = archivo.readlines ()
print(números2)
archivo.close()


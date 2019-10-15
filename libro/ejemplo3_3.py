CUECER = 0
N = int(input("Dame un número entero positivo: "))
for I in range (0,N,1):
    NUM = int(input("ingresa un entero: "))
    if NUM == 0:
        CUECER += 1
print("El número de ceros capturados fue: ", CUECER)

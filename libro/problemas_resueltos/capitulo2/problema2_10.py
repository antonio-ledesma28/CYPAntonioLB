A = int(input("intodruce un valor entero positivo: "))
B = int(input("introduce otro valor de tipo entero positivo: "))
C = int(input("introduce otro valor de tipo entero positivo: "))
if A > B :
    if A > C :
        print("A es mayor con valor de {A}")
    elif A == C :
        print(f"A y C son iguales a {A} y son los mayores")
    else:
        print(f"C que vale {C} es el mayor")
elif A == B:
    if A > C :
        print(f"A y B son los mayores con valor {A}")
    elif A == C:
        print(f"A, B y C son iguales con valor {A}")
    else :
        print (f"C es el mayor con valor de {C}")
elif B > C :
    print(f"B es el mayor con valor de {B}")
elif B == C :
        print(f"B y C son los mayores con valor {B}")
else:
    print(f"C es el mayor valor {C}")
    print("Fin del programa")

        

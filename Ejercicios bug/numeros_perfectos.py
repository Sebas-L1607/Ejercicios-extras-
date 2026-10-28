
def perfecto(numper):
    if numper % 2 == 0:
        print ("\nEl numero es un numero perfecto\n")
    else:
        print ("\nEl numero no es un numero perfecto\n")


while True: 

    numper = int(input("\nIngrese el numero para saber si es perfecto.\n"))


    if numper <0:
        print ("\nEl ejercicio se ha acabado\n\n")
        break

    elif 0<= numper <=2:
        print("\nLos numeros a buscar tienen que ser diferentes a 0, 1 y 2\n")
        
    else:
        perfecto(numper)
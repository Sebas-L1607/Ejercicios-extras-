def menu ():
    print("""
REGISTRO DE TEMPERATURA DE LAS TORTUGAS MARINAS

Digita la accion que quieres hacer

1. Registrar temperatura

0. Salir del sistema

""")

def menu1 ():
    print("""


1. Registrar temperatura

0. Salir del sistema

""")

def elegir ():
    opcion = int(input("Que accion quiere hacer? "))
    while opcion != 0 and opcion != 1:
        print("Favor de seleccionar 1 de las dos opciones")
        menu1 ()
        opcion = int(input("Que accion quiere hacer? "))

    return opcion

def temperatura():
    temp = float(input("Favor de digitar la temperatura del huevo de tortuga: "))

    if temp < 26:
        print ("\n\n***** ALERTA ****\n\nLa temperatura es BAJA \n\n Recuerde que la mejor temperatura esta entre los 26 y 34 grados.")

    elif temp > 32:
        print ("\n\n***** ALERTA ****\n\nLa temperatura es ALTA \n\n Recuerde que la mejor temperatura esta entre los 26 y 34 grados.")
    
    else:
        print("\n\nEl huevo se encuentra en una temperatura NORMAL.\n\n")

while True: 
    menu()
    opcion = elegir()

    match opcion:

        case 0: 
            print("Has salido del programa del registro de temperaturas.")
            break
        case 1:
            temperatura ()


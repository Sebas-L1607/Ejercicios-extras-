while True:
    norig = int(input("Ingrese un numero: \n"))

    if norig <= 0:
        print ("Programa terminado")
        break

    n = norig
    cont = 0

    while n > 0:
        cont = cont + 1
        n = n // 10

    suma = 0
    n = norig

    while n >= 10: 
        dig = n % 10
        suma = suma + (dig ** cont)
        n = n // 10


    suma = suma + (n ** cont)

    if suma == norig: 
        print ("El numero es narcicista")
    else: 
        print("El numero no es narcisista")

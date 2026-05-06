import random






while InterfazMostrando:
    print("Bienvenido a Calculadora")
    print("1.-Suma") 
    print("2.-Resta")
    print("3.-Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
       seguir=True
       while seguir:
        print("Suma")
        numero1=int(input("Ingrese numero uno: "))
        numero2=int(input("Ingrese numero dos: "))
        resultado = numero1+numero2
        print('El resultado de la suma es de: ',resultado)
        resultado = 0
        numero1 = 0
        numero2 = 0

        terminar=input('Desea hacer otra suma (Si/No)')
        if terminar == "Si":
            seguir = True
        
        

    if opcion == 2:
        print('Resta')
        numero1=int(input("Ingrese numero uno: "))
        numero2=int(input("Ingrese numero dos: "))
        resultado = numero1-numero2
        print('El resultado de la resta es de: ',resultado)
        resultado = 0
        numero1 = 0
        numero2 = 0
        terminar=input('Desea hacer otra operacion (Si/No)')
        if terminar == "No":
            opcion = 3
        
       
    if opcion == 3:
        InterfazMostrando = False
        print("Saliendo")

    if opcion > 3 or opcion < 1:
        print("Ingrese datos validos")



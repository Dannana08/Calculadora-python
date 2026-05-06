print("CALCULADORA")
print("-" * 30)

while True:
    print ("1.suma")
    print ("2. resta")
    print ("3.multiplicacion")
    print ("4. division")
    print ("5.salir")
    print ("-" * 30)

    opcion = int(input("ingrese una opcion: "))

    if opcion == 1:
        print("suma")
        print ("-" * 30)

        num1=float(input("ingrese el primer numero: "))
        num2=float(input("ingrese el segundo numero: "))

        resultado= num1 + num2
        print ("-" * 30)

        print(f"el resultado de la suma es: {resultado}")        
    
    elif opcion == 2:     
         print("resta")
         print ("-" * 30)

         num1=float(input("ingrese el primer numero: "))
         num2=float(input("ingrese el segundo numero: "))
         
         resultado= num1 - num2
         print ("-" * 30)

         print(f"el resultado de la resta es: {resultado}")

    elif opcion == 3:
         print("multiplicar")
         print ("-" * 30)

         num1=float(input("ingrese el primer numero: "))
         num2=float(input("ingrese el segundo numero: "))

         resultado= num1 * num2
         print ("-" * 30)

         print(f"el resultado de la multiplicacion es: {resultado}")

    elif opcion == 4:
         print("dividir")
         print ("-" * 30)

         num1=float(input("ingrese el primer numero: "))
         num2=float(input("ingrese el segundo numero: "))

         

         if num2 == 0:
              print("no puede dividir por cero")

         else: 
             resultado= num1 / num2
             print ("-" * 30)
             
             print(f"el resultado de la division es: {resultado}") 

    elif opcion == 5:
         print ("saliendo...")
         print ("-" * 30)
         break
    else:
         print("ingrese una opcion valida")           



                                      


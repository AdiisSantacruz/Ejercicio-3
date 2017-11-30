import os
pi = 3.14
res = 0
salir = False

def funcion():
    print ("Menu")
    print ("Calculo de areas")
    print ("1.- Circulo")
    print ("2.- Cuadrado")
    print ("3.- Rectangulo")
    print ("4.- Triangulo")
    print ("5.- Salir")

while True:

    funcion()
    op = int(input("Seleccione un opcion"))

    if op == 1:
        radio = float(input("Ingrese el radio del circulo"))
        res = pi * (radio * radio)
        print("El area del circulo es: " + str(res))


    elif op == 2:
        la1 = float(input("Ingrese la altura del cuadrado"))
        la2 = float(input("Ingrese la del base"))
        res = la1 * la2
        print("El area del cuadrado es: " + str(res))


    elif op == 3:
        la1r = float(input("Ingrese la altura del cuadrado"))
        la2r = float(input("Ingrese la base"))
        res = la1r * la2r
        print("El area del resctangulo es: " + str(res))


    elif op == 4:
        alt = float(input("Ingrese la altura del triangulo"))
        baset = float(input("Ingrese la base del triangulo"))
        res = (baset * alt) / 2
        print("El area del resctangulo es: " + str(res))

    elif op == 5:
        break
    else:
        print ("Opcion no valida :v seleccione una opcion correcta")
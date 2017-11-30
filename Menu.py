pi = 3.14
res = 0
print ("Menu")
print ("Calculo de areas")
print ("1.- Circulo")
print ("2.- Cuadrad")
print ("3.- Rectangulo")
print ("4.- Triangulo")
print("5.- Salir")

op = int(input("Seleccione un opcion"))

while(op != 5):
    if op == 1:
        radio = int(input("Ingrese el radio del circulo"))
        res = pi * (radio*radio)
        print("El area del circulo es: " + str(res))


la1 = int(input("Ingrese la altura del cuadrado"))
la2 = int(input("Ingrese la altura del base"))
la1r = int(input("Ingrese la altura del cuadrado"))
la2r = int(input("Ingrese la base"))
alt = int(input("Ingrese la altura del triangulo"))
baset = int(input("Ingrese la base del triangulo"))


import math

def mostrar_menu():
    print("Menú:")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Circunferencia")
    print("4. Salir")

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_perimetro_cuadrado(lado):
    return lado * 4

def calcular_area_circunferencia(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circunferencia(radio):
    return 2 * math.pi * radio


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        perimetro = calcular_perimetro_triangulo(base, altura/2, math.sqrt((base/2)**2 + altura**2))
        print("El área del triángulo es:", area)
        print("El perímetro del triángulo es:", perimetro)

    elif opcion == "2":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        perimetro = calcular_perimetro_cuadrado(lado)
        print("El área del cuadrado es:", area)
        print("El perímetro del cuadrado es:", perimetro)

    elif opcion == "3":
        radio = float(input("Ingrese el radio de la circunferencia: "))
        area = calcular_area_circunferencia(radio)
        perimetro = calcular_perimetro_circunferencia(radio)
        print("El área de la circunferencia es:", area)
        print("El perímetro de la circunferencia es:", perimetro)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, por favor ingrese una opción válida.")

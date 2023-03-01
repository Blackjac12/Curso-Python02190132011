
total_ventas = 0
promedio_ventas = 0


lunes = float(input("Ingrese las ventas del Lunes: "))
martes = float(input("Ingrese las ventas del Martes: "))
miercoles = float(input("Ingrese las ventas del Miércoles: "))
jueves = float(input("Ingrese las ventas del Jueves: "))
viernes = float(input("Ingrese las ventas del Viernes: "))
sabado = float(input("Ingrese las ventas del Sábado: "))
domingo = float(input("Ingrese las ventas del Domingo: "))


total_ventas = lunes + martes + miercoles + jueves + viernes + sabado + domingo


promedio_ventas = total_ventas / 7


print("El total de ventas de la semana es:", total_ventas)
print("El promedio de ventas de la semana es:", promedio_ventas)

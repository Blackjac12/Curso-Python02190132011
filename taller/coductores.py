conductor_km = {}

while True:
    # Pedir el nombre del conductor y los kilómetros conducidos en una semana
    conductor = input("Ingrese el nombre del conductor: ")
    km_semana = float(input("Ingrese los kilómetros conducidos esta semana por el conductor: "))

    # Verificar si el conductor ya está en el diccionario
    if conductor in conductor_km:
        # Si el conductor ya está en el diccionario, sumar los kilómetros
        conductor_km[conductor] += km_semana
    else:
        # Si el conductor no está en el diccionario, agregarlo con los kilómetros de la semana
        conductor_km[conductor] = km_semana

    # Preguntar si se desea agregar más conductores
    seguir = input("¿Desea ingresar más conductores? (s/n): ")
    if seguir.lower() == "n":
        break

# Imprimir los resultados
print("Kilómetros conducidos por conductor:")
for conductor, km in conductor_km.items():
    print(f"{conductor}: {km} km")

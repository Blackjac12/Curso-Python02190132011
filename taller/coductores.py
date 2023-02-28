# Creamos variables para almacenar los nombres de los conductores y sus kilómetros conducidos
conductor1_km_lunes = int(input("Kilómetros conducidos por conductor 1 el lunes: "))
conductor1_km_martes = int(input("Kilómetros conducidos por conductor 1 el martes: "))
conductor1_km_miercoles = int(input("Kilómetros conducidos por conductor 1 el miércoles: "))
conductor1_km_jueves = int(input("Kilómetros conducidos por conductor 1 el jueves: "))
conductor1_km_viernes = int(input("Kilómetros conducidos por conductor 1 el viernes: "))

conductor2_km_lunes = int(input("Kilómetros conducidos por conductor 2 el lunes: "))
conductor2_km_martes = int(input("Kilómetros conducidos por conductor 2 el martes: "))
conductor2_km_miercoles = int(input("Kilómetros conducidos por conductor 2 el miércoles: "))
conductor2_km_jueves = int(input("Kilómetros conducidos por conductor 2 el jueves: "))
conductor2_km_viernes = int(input("Kilómetros conducidos por conductor 2 el viernes: "))

conductor3_km_lunes = int(input("Kilómetros conducidos por conductor 3 el lunes: "))
conductor3_km_martes = int(input("Kilómetros conducidos por conductor 3 el martes: "))
conductor3_km_miercoles = int(input("Kilómetros conducidos por conductor 3 el miércoles: "))
conductor3_km_jueves = int(input("Kilómetros conducidos por conductor 3 el jueves: "))
conductor3_km_viernes = int(input("Kilómetros conducidos por conductor 3 el viernes: "))

conductor4_km_lunes = int(input("Kilómetros conducidos por conductor 4 el lunes: "))
conductor4_km_martes = int(input("Kilómetros conducidos por conductor 4 el martes: "))
conductor4_km_miercoles = int(input("Kilómetros conducidos por conductor 4 el miércoles: "))
conductor4_km_jueves = int(input("Kilómetros conducidos por conductor 4 el jueves: "))
conductor4_km_viernes = int(input("Kilómetros conducidos por conductor 4 el viernes: "))

# Podemos realizar operaciones con estas variables para calcular las cantidades que necesitemos
total_km_conductor1 = conductor1_km_lunes + conductor1_km_martes + conductor1_km_miercoles + conductor1_km_jueves + conductor1_km_viernes

print("El conductor 1 condujo un total de", total_km_conductor1, "kilómetros durante la semana.")

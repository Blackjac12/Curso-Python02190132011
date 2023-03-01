def calcular_nota_final(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# Variables para el resumen
aprobados = 0
reprobados = 0
suma_notas_finales = 0

while True:
    # Pedir datos del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la nota de la primera evaluación: "))
    nota2 = float(input("Ingrese la nota de la segunda evaluación: "))
    nota3 = float(input("Ingrese la nota de la tercera evaluación: "))

    # Calcular nota final
    nota_final = calcular_nota_final(nota1, nota2, nota3)

    # Presentar resultados
    print("El estudiante", nombre, "obtuvo una nota final de", nota_final)

    # Actualizar resumen
    suma_notas_finales += nota_final
    if nota_final >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

    # Preguntar si desea continuar ingresando datos
    respuesta = input("¿Desea continuar ingresando datos? (S/N): ")
    if respuesta == "N" or respuesta == "n":
        break

# Presentar resumen final
total_estudiantes = aprobados + reprobados
promedio_notas_finales = suma_notas_finales / total_estudiantes

print("Resumen:")
print("Total estudiantes:", total_estudiantes)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio notas finales:", promedio_notas_finales)

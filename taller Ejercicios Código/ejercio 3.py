
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Ingrese un número entero positivo: "))

fact = factorial(n)


cant_pares = 0
cant_impares = 0
acum_pares = 0
acum_impares = 0

# Recorrer los números desde 1 hasta n
for i in range(1, n+1):
    # Verificar si el número es par o impar
    if i % 2 == 0:
        cant_pares += 1
        acum_pares += i
    else:
        cant_impares += 1
        acum_impares += i

# Presentar resultados
print("El factorial de", n, "es:", fact)
print("Cantidad de números pares:", cant_pares)
print("Cantidad de números impares:", cant_impares)
print("Valor acumulado de los pares:", acum_pares)
print("Valor acumulado de los impares:", acum_impares)

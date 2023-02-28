# Leemos las cantidades de cada artículo para cada sucursal
suc1_art1 = int(input("Cantidad artículo 1 en sucursal 1: "))
suc1_art2 = int(input("Cantidad artículo 2 en sucursal 1: "))
suc1_art3 = int(input("Cantidad artículo 3 en sucursal 1: "))
suc1_art4 = int(input("Cantidad artículo 4 en sucursal 1: "))
suc1_art5 = int(input("Cantidad artículo 5 en sucursal 1: "))
suc2_art1 = int(input("Cantidad artículo 1 en sucursal 2: "))
suc2_art2 = int(input("Cantidad artículo 2 en sucursal 2: "))
suc2_art3 = int(input("Cantidad artículo 3 en sucursal 2: "))
suc2_art4 = int(input("Cantidad artículo 4 en sucursal 2: "))
suc2_art5 = int(input("Cantidad artículo 5 en sucursal 2: "))
suc3_art1 = int(input("Cantidad artículo 1 en sucursal 3: "))
suc3_art2 = int(input("Cantidad artículo 2 en sucursal 3: "))
suc3_art3 = int(input("Cantidad artículo 3 en sucursal 3: "))
suc3_art4 = int(input("Cantidad artículo 4 en sucursal 3: "))
suc3_art5 = int(input("Cantidad artículo 5 en sucursal 3: "))
suc4_art1 = int(input("Cantidad artículo 1 en sucursal 4: "))
suc4_art2 = int(input("Cantidad artículo 2 en sucursal 4: "))
suc4_art3 = int(input("Cantidad artículo 3 en sucursal 4: "))
suc4_art4 = int(input("Cantidad artículo 4 en sucursal 4: "))
suc4_art5 = int(input("Cantidad artículo 5 en sucursal 4: "))

# Calculamos las cantidades totales de cada artículo
art1_total = suc1_art1 + suc2_art1 + suc3_art1 + suc4_art1
art2_total = suc1_art2 + suc2_art2 + suc3_art2 + suc4_art2
art3_total = suc1_art3 + suc2_art3 + suc3_art3 + suc4_art3
art4_total = suc1_art4 + suc2_art4 + suc3_art4 + suc4_art4
art5_total = suc1_art5 + suc2_art5 + suc3_art5 + suc4_art5

# Calculamos la cantidad de artículos en sucursal 2
articulos_sucursal2 = suc2_art1 + suc2_art2 + suc2_art3 + suc2_art4 + suc2_art5

# Calculamos la cantidad del artículo 3 en la sucursal 1
art3_sucursal1 = suc1_art3

# Calculamos la recaudación total de cada sucursal
sucursal1_recaudacion = suc1_art1*precio_art1 + suc1_art2*precio_art2 + suc1_art3*precio_art3 + suc1_art4*precio_art4 + suc1_art5*precio_art5
sucursal2_recaudacion = suc2_art1*precio_art1 + suc2_art2*precio_art2 + suc2_art3*precio_art3 + suc2_art4*precio_art4 + suc2_art5*precio_art5
sucursal3

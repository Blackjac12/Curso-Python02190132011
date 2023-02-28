# Leemos los precios y las cantidades de cada artículo para cada sucursal
art1_precios = []
art2_precios = []
art3_precios = []
art4_precios = []
art5_precios = []
art1_cantidades = []
art2_cantidades = []
art3_cantidades = []
art4_cantidades = []
art5_cantidades = []

for i in range(4):
    print(f"Sucursal {i+1}:")
    precio = float(input("Precio artículo 1: "))
    art1_precios.append(precio)
    cantidad = int(input("Cantidad artículo 1: "))
    art1_cantidades.append(cantidad)
    precio = float(input("Precio artículo 2: "))
    art2_precios.append(precio)
    cantidad = int(input("Cantidad artículo 2: "))
    art2_cantidades.append(cantidad)
    precio = float(input("Precio artículo 3: "))
    art3_precios.append(precio)
    cantidad = int(input("Cantidad artículo 3: "))
    art3_cantidades.append(cantidad)
    precio = float(input("Precio artículo 4: "))
    art4_precios.append(precio)
    cantidad = int(input("Cantidad artículo 4: "))
    art4_cantidades.append(cantidad)
    precio = float(input("Precio artículo 5: "))
    art5_precios.append(precio)
    cantidad = int(input("Cantidad artículo 5: "))
    art5_cantidades.append(cantidad)

# Calculamos las cantidades totales de cada artículo
art1_total = sum(art1_cantidades)
art2_total = sum(art2_cantidades)
art3_total = sum(art3_cantidades)
art4_total = sum(art4_cantidades)
art5_total = sum(art5_cantidades)

# Calculamos la cantidad de artículos en sucursal 2
articulos_sucursal2 = art1_cantidades[1] + art2_cantidades[1] + art3_cantidades[1] + art4_cantidades[1] + art5_cantidades[1]

# Calculamos la cantidad del artículo 3 en la sucursal 1
art3_sucursal1 = art3_cantidades[0]

# Calculamos la recaudación total de cada sucursal
sucursal1_recaudacion = sum([art1_precios[0]*art1_cantidades[0], art2_precios[0]*art2_cantidades[0], art3_precios[0]*art3_cantidades[0], art4_precios[0]*art4_cantidades[0], art5_precios[0]*art5_cantidades[0]])
sucursal2_recaudacion = sum([art1_precios[1]*art1_cantidades[1], art2_precios[1]*art2_cantidades[1], art3_precios[1]*art3_cantidades[1], art4_precios[1]*art4_cantidades[1], art5_precios[1]*art5_cantidades[1]])
sucursal3_recaudacion = sum([art1_precios[2]*art1_cantidades[2], art2_precios[2]*art2_cantidades[2], art3_precios[2]*art3_cantidades[2], art4_precios[2]*art4_cantidades[2], art5_precios[2]*art5_cantidades[2]])

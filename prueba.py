num = int(input("Ingrese el nuemro "))

if num < 0 :
    print("el nnumeor nos validod")
else:
    suma = 0
    for i in  range(num+1):
        suma += i
    print ("suma de rango que va desde 0 hasta ",num,"es",suma)    

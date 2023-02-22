while True:
    print("digite la letra 'A' para Actukizar Sistemas")
    print("digite la letra 'E' para Eliminar catalogo")
    print("digite la letra 'S' para salir del programa")
    letra=str(input())
    
    if letra=='S' or letra=='s':
        print("finilizo con exito \n")
        break
    elif letra== 'A' or letra=='a':
        print ("se actulizado el sistema \n ")
    elif letra=='E' or letra=='e':
        print("se a eliminado un catalogo \n")    


print ("EL DO-WHILE a finilizado \n")
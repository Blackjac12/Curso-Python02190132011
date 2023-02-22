suma=0

for i in range(0,12,2):
    print ("digite el numero" + str(i+1)+":")
    numero = int(input())   
    suma = suma+numero

print("la sumatoria total es: "+ str(suma))
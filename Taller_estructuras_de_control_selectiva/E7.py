"""
Entradas
distancia-->float-->km
Salidas
deuda por pagar-->float-->dp

"""
km=float(input("Digite distancia recorrida "))

if (km<300):
    print("Se deben pagar 50.000 ")  
elif(km>=300) and (km<=1000):
    total=(km-300)*30000+70000

    print("La deuda es de: "+str(total))
    
elif(km>1000):
    total=(km-300)*9000+150000
    print("La deuda es de: "+str(total))
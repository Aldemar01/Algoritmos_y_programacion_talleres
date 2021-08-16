"""
Entradas:
cantidad de naranjas--->int--->X
p por doce--->float--->Y
valor venta--->float--->K
Salidas:
numero de docenas--->float--->doce
costo--->float--->p
gan--->float--->ganancia
porc gan--->float--->porc
"""
X=int(input ("Numero de naranjas: "))
Y=float(input ("Valor por doce: "))
K=float(input ("Valor de las ventas: "))
doce=(X/12)
p=(Y*doce)
gan=(K-p)
porc=((gan*100)/p)
print("El porcentaje de ganancia es: "+str(porc), "%")
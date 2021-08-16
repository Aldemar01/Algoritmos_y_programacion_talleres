"""
Entradas:
precio de contado--->float--->P
valor de la cuota mensual--->float--->T
Salidas:
precio cuotas--->float--->precio
recargo--->float--->recargo
porcentaje de recargo--->float--->porcentaje
"""
P=float(input ("Precio de contado:" ))
T=float(input ("Valor de la cuota: "))
precio=(T*12)
recargo=(precio-P)
porcentaje=((recargo*100/P))
print("El porcentaje es de: "+str(porcentaje), "%")
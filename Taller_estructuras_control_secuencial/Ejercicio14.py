"""
Entradas:
lectura actual--->float--->l2
lectura anterior--->float--->l1
valor kw--->float--->vkw
Salidas:
consumo--->float--->con
total factura-->float--->tot
"""
l2=float(input ("Digite lectura actual: "))
l1=float(input ("Digite lectura anterior: "))
vkw=float(input ("Valor del kw es de: "))
con=(l2-l1)
tot=(con*vkw)
print("El valor a pagar es de: "+str(tot))

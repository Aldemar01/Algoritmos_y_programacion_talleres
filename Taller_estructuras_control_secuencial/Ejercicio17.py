"""
Entradas:
Presupuesto total--->float--->prep
Salidas:
presupuesto ginecologia--->float--->gine
presupuesto traumatologia--->float--->traum
presupuesto pediatria--->float--->ped
"""
prep=float(input ("Digite el valor del presupuesto total anual "))
gine=(prep*0.4)
traum=(prep*0.3)
ped=(prep*0.3)
print("El presupuesto de ginecologia es: "+str(ginecologia))
print("El presupuesto de traumatologia es: "+str(traumatologia))
print("El presupuesto de pediatria es: "+str(pediatria))
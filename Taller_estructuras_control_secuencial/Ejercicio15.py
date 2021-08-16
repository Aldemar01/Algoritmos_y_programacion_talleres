"""
Entradas:
precio final--->float--->pf
precio de venta--->float--->pv
Salidas:
diferencia--->float--->dif
porcentaje descuento--->float--->desc
"""
pf=float(input ("Digite el valor pagado: "))
pv=float(input ("Ingrese el precio de venta sugerido: "))
dif=(pv-pf)
desc=((dif*100)/pv)
print("El porcentaje de descuento fue: "+str(desc))
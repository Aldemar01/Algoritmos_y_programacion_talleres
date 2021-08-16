"""
Entradas:
Capital-->float-->cap
time-->int-->time
tasa-->float-->Tasa
Salidas:
Interes-->float-->Interes
Promedio-->float-->prom
"""
Cap=float(input("Insertar capital: "))
time=int(input("Insertar el time de inversión: "))
Tasa=float(input("Insertar la tasa de interes: "))
Interes=((Cap*Tasa*time)/100)
Prom=(Interes/time)
print("El valor total de interes es: "+ str(Interes), "El porcentaje de interes al año es: "+ str(Prom), "%")

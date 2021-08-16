"""
Entradas:
Horas trabajadas--->float--->h
prec--->float--->prec
Salidas:
Salario bruto--->float--->sbr
descuentos--->float--->desc
salario neto--->float--->st
"""
h=float(input("Ingrese el numero de horas trabajadas: "))
prec=float(input("Ingrese el valor por cada hora de trabajo: "))
sbr=(h*prec)
desc=(sbr*0.2)
st=(sbr-desc)
print("El salario total es de: "+str(st))
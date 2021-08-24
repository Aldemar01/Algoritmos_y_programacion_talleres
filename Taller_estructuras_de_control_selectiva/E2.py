"""
Entradas
salario_bruto-->float-->sb
Salidas
salario_neto-->float-->sn
"""
sb=float(input("Digite salario bruto: "))
if(sb<900000):
  cn=sb+(sb*0.15)
  print("El salario neto es: "+str(cn))
else:
  cn=sb+(sb*0.12)
  print("El salario neto es: "+str(cn))
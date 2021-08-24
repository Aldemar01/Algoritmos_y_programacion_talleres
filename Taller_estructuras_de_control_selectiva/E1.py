"""
Entradas
Capital_invertir-->float-->ci 
Salidas
Tasa_interes-->float-->ti
"""
ci=float(input("Capital a invertir "))
ti=float(input("Tasa de interes "))
if(ci>100000):
 g=(ci*ti)
print("La ganancia sera de: "+str(g))
g1=ci+g
print("El dinero total que esta en la cuenta sera de: " +str(g1))


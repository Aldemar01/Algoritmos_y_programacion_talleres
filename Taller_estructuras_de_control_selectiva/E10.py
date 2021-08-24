
"""
Entradas
salario-->int-->s
categoria-->int-->c
Salidas
aumento-->int-->a
salario nuevo-->int-->sn
""" 
s=int(input("Digite el salario:") ) 
c=int(input("Digite una categoria del 1 al 5: ")) 
if (c==1):
  a=s*.10
if (c==2): 
  a=s*.15 
if (c==3):
  a=s*.20
if (c==4): 
 a=s*.40
 if (c==5): 
  a=s*.60 

sn=s+a
 
print("El aumento sera: "+str(a))
print("Valor de el sueldo nuevo: " +str(sn))
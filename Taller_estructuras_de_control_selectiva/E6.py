"""
Entradas
variable1-->int-->v1
variable2-->int-->v2
variable3-->int-->v3
variable4-->int-->v4
Salidas
miles-->int-->m
decenas-->int-->d
numero-->int-->n
"""
v1=int(input("Digite el valor de la variable A: "))
v2=int(input("Digite el valor de la variable B: "))
v3=int(input("Digite el valor de la variable C: "))
v4=int(input("Digite el valor de la variable D: "))

if (v3>=5):
  m=v1*1000
  d=v2*100
  n=m+(d+100)
  print(n)
else:
  m=v1*1000
  ds=v2*100
  n=m+(d+100)
  print(n) 
 
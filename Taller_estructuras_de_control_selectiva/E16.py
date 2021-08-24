"""
Entradas
A-->int
B-->int
C-->int
Salidas
D-->int
"""
import math
A=int(input("Digite el valor de A: "))
B=int(input("Digite el valor de B: "))
C=int(input("Digite el valor de C: "))
D=((B**2)-(4*A*C))
if(D==0):
  X1=(-B/(2*A))
  X2=(-B/(2*A))
  print("Los valores de X1 y X2 son: "+str(  X1,X2))
elif(D>0):
  X2=(-B+math.sqtr((B**2)-(4*A*C)))/(2*A)
  X3=(-B+math.sqtr((B**2)-(4*A*C)))/(2*A)
 print("Los valores de X2 y X3 son: " +str(X2,X3))
elif(D<0):
  print("No tiene solucion los reales")
else:
  print("Error")

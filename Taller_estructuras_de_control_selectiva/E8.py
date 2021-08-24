"""
Entradas
valor entero 1-->int-->v1
valor entero 2-->int-->v2
salidas
valores de v1 u v2
"""
v1=int(input("Digite el valor del entero: "))
v2=int(input("Digite el valor del entero: "))

 

expre=(v1**3+v2**4-2*v1**2)
    
if (expre<=680):
   print("X y Y satisfacen la expresión "+str(expre)) 
elif(expre>=680):
    print("La expresion es mayor a 680 ")
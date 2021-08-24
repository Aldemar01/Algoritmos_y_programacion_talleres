"""
Entradas
salario=>int=>s
ventas departamento 1-->int-->vd1
ventas departamento 2-->int-->vd2
ventas departamento 3-->int-->vd3
salidas
venta total mes departamentos-->int-->ventotal
"""
s=int(input("ingrese salario "))
vd1=int(input("ingrese ventas echas "))
vd2=int(input("ingrese ventas echas "))
vd3=int(input("ingrese ventas echas "))

ventotal=(vd1+vd2+vd3)
print("venta total: "+str(ventotal))
e33=(ventotal*33)/100

if(vd1>e33):
    vd1=s+s*.20
else:
    vd1=s
print("los vendedores del departamento 1 recibiran: "+str(vd1))    
    
if(vd2>e33):
    vd2=s+s*.20
else:

    vd2=s   
print("los vendedores del departamento 2 recibiran: "+str(vd2))    
if(vd3>e33):
    vd3=s+s*.20
else:
    vd3=s        
print("los vendedores del departamento 3 recibiran: "+str(vd3))  
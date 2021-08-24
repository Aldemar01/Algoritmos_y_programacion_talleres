"""
Entradas
cantidadpiezas-->float-->cp 
valor de la pieza-->float-->vp
Salidas 
inversion-->float-->i
banco-->float-->b
credito-->float-->c
interes-->float-->int
"""
cp=float(input("Digite la cantidad de piezas a comprar: "))
vp=float(input("Digite el valor por pieza: "))
t=(cp*vp)
if (t>5000000):
  i=(t*0.55)
  b=(t*0.30)
  c=(t*0.15)
  print("La inversion sera de: " +str(i))
  print("El prestamo del banco sera de: " +str(b))
  print("El credito a pagar es: " +str(c))
else:
  i=(t*0.70)
  b=(0)
  c=(t*0.30)
  print("La inversion sera de: " +str(i))
  print("El prestamo del banco sera de: " +str(b))
  print("El credito a pagar es: " +str(c))

int=(c*0.20)
print("El interes por el credito es de: " +str(int))
 
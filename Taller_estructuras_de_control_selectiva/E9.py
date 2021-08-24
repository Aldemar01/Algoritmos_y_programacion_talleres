"""
Entradas
nombre-->float-->n
Costo-->float-->c
Salidas
Descuento-->float-->d
Descuento2-->float-->d2

"""
n=input("Digite su nombre: ")
c=float(input("Digite el valor del producto: "))

if c<50000:
  d=0
  d2=c*d
  f=c-d2

if c>50000 <=100000:
  d=0.5
  d2=c*d
  f=c-d2

if c>100000 <=700000:
  d=0.11
  d2=c*d
  f=c-d2

if c>700000 <=1500000:
  d=0.18
  d2=c*d
  f=c-d2

if c>1500000:
  d=0.25
d2=c*d
f=c-d2

print("Cliente:", n,
"El costo del producto es: ",str(c),
"El precio final sera de:",str(f),
"El descuento es de: ",str(d2,))
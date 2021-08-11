line = input().split()
a,b,c= line
a= float(a)
b= float(b)
c= float(c)
tr= (a*c)/2
cir= 3.14159*c**2
tra= ((a+b)/2)*c
cua= b**2
rec= a*b
print("TRIANGULO: ""{:.3f}".format (tr))
print("CIRCULO: ""{:.3f}".format (cir))
print("TRAPEZIO: ""{:.3f}".format (tra))
print("QUADRADO: ""{:.3f}".format (cua))
print("RETANGULO: ""{:.3f}".format (rec))
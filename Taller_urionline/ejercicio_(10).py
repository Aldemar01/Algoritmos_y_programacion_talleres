Name=str(input("Por favor escriba su nombre: "))
bn=float(input("Por favor ingrese su salario fijo: "))
vt=float(input("Ingrese su numero de ventas este mes: "))
qc=(vt*0.15)
tl=(qc+bn)
print("TOTAL = R$ ""{:.2f}".format (tl))
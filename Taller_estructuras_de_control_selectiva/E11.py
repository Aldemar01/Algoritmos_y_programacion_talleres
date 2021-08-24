"""
Entradas
temperatura-->float-->t
Salidas
tipo de natacion-->str-->tn
"""
t=float(input("Digite temperatura :"))
if(t>85):
  print("Natacion")
elif(t>71 and t<=85):
  print("Tenis")
elif(t>33 and t<=70):
  print("Golf")
elif(t>11 and t<=32):
  print("Esqui")
elif(t<=10):
  print("Marcha")
else:
  print("No se indentifico ningun deporte")
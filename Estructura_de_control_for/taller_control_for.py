archivo = open('paises.txt', 'r')
#1.imprima la posicion de colombia
"""
co=0
list1=[]
for i in archivo:
  list1.append(i)
  a=" ".join(list1)
  co=co+1 
  if(a=="Colombia: Bogotá\n"):
    break
  list1=[]   
print(co)
"""

#2.Imprima todos los paises
"""
list1=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    list1.append(i[r])
  a="".join(list1)
  print(a)
  list1=[]
"""

#3.Imprima todas las Capitales
"""
list1=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    list1.append(i[r])
  a="".join(list1)
  print(a)
  list1=[]
"""  
#4.Imprimir todos los paises que inicien con la letra C
"""
list1=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    list1.append(i[r])
  a="".join(list1)
  paises.append(a)
  list1=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
  """

#5.imprima todas las capitales que inicien con la leta B
"""
list1=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    list1.append(i[r])
  a="".join(list1)
  ciudad.append(a)
  list1=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""

#6.Cuente e imprima cuantas ciudades inician con la letra M
"""  
list1=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    list1.append(i[r])
  a="".join(list1)
  ciudad.append(a)
  list1=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i)
"""

#7.Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
list1=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    list1.append(i[r])
  a="".join(list1)
  pais.append(a)
  list1=[]
for i in pais:
  if(i[0]=="U"):
    print(i)
list2=[]
capital=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    list1.append(i[r])
  a="".join(list1)
  capital.append(a)
  list1=[]
for i in capital:
  if(i[0]=="u"):
    print(i)
"""

#8.Cuente e imprima cuantos paises que hay en el archivo
"""
c=0
list1=[]
for i in archivo:
  list1.append(i)
  a="".join(list1)
  c=c+1
print(len(list1))
"""

#9.Busque e imprima la ciudad de Singapur
"""
list1=[]
for i in archivo:
  list1.append(i)
  a=" ".join(list1)
  if(a=="Singapur: Singapur\n"):
    break
  list1=[]   
print(a)
"""

#10.Busque e imprima el pais de Venezuela y su capital
"""
list1=[]
for i in archivo:
  list1.append(i)
  a=" ".join(list1)
  if(a=="Venezuela: Caracas\n"):
    break
  list1=[]   
print(a)
"""

#11.Cuente e imprima las ciudades que su pais inicie con la letra E
"""
list1=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    list1.append(i[r])
  a="".join(list1)
  ciudad.append(a)
  list1=[]
for i in ciudad:
  if(i[0]=="E"):
    print(i)
"""

#12.Busque e imprima la Capital de Colombia
"""
palabra="Colombia:Bogotá"
a=palabra.index(":")
list1=[]
for i in range(a+1,len(palabra)):
  list1.append(palabra[i])
unir="".join(list1)
print(unir)
"""

#13.imprima la posicion del pais de Uganda
"""
c=0
list1=[]
for i in archivo:
  list1.append(i)
  a=" ".join(list1)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  list1=[]   
print(c)
"""

#14.imprima la posicion del pais de Mexico
"""
x=0
list1=[]
for i in archivo:
  list1.append(i)
  a=" ".join(list1)
  x=x+1 
  if(a=="México: Ciudad de México \n"):
    break
  list1=[]   
print(x)
"""

#15.El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
list1=[]
for i in archivo:
  list1.append(i)
  a="".join(list1)
  if(a=="Madagascar: rey julien\n"):
    break
list2=[]
for i in archivo:
  a=i.index(":")
for i in range(0,len(i)):
  list2.remove("rey julien")
  list2.insert("Madagascar: Antananarivo")
  print(list2)
"""

#16.Agregue un país que no esté en la lista
"""
c=0
list1=[]
for i in archivo:
  list1.append(i)
  a=" ".join(list1)
  c=c+1 
  if(a=="Paises\n"):
    break
b=a.index(":")
list2=[] 
for i in range(0,len(a)):
      list2.append(a[i])
list2.insert(0,"República de Gorteau del Oeste: Peijin \n")
unir="".join(list2)
print(unir)
"""
archivo.close()
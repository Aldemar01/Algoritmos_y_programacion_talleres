frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las listas con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las listas con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elmentos de la lista
"""
Entradas:
lista-->list-->l1
elemento->str-->elm
Salidas
lista-->l1
"""
def eliminar_un_caracter(l1,elm):
  auxilar=[]
  for i in l1:
    a=i.replace(elm,"")
    auxilar.append(a)
  return auxilar
 

#Realizar una funcion que retorne la copia de una lista que pasa por parametro 
"""
Entradas:
lista-list-->l1
Salidas
lista-list-->l1
"""
def copia_lista(l1):
  return l1.copy() 
#Realizar una funcion que retorne una lista de numeros enteros  
"""
Entradas:
lista-list-->l1
Salidas
lista-list-->l1
"""   
def numeros_enteros(l1):
  aux=[]
  aux_uno=[]
  for i in l1:
    aux.append(float(i))
  for i in aux:
    aux_uno.append(int(i))  
  return aux_uno

#Realiza una funcion que retorne una lista con los numeros pares
"""
Entradas:
lista-list-->l1
Salidas
lista-list-->l1
"""  
def numeros_pares(l1):
  aux=[]
  for i in l1:
    if(float(i)%2==0):
      aux.append(i)
  return aux    
#Realizar una funcion que elimine un elm de una lista
"""
Entradas:
lista-list-->l1
elm-->str-->elm
Salidas
lista-list-->l1
"""  
def elimina_elemento_lista(l1,elm):
  l1.remove(elm)
  return l1


#Retorna una l1 con las palabras iniciales con la l etra que pasa por parametro  
"""
Entradas:
lista-list-->l1
letra-->str-->let
Salidas
lista-list-->l1
"""  
def palabras_por_letra (l1,elm):
  aux=[]
  for i in l1:
     if(i[0]==elm):
      aux.append(i)
  return aux


#Realizar una funcion que retorne el tamaño de una lista  
"""
Entradas:
lista->list->l1
Salidas
tamaño-->int->tm
"""   
def tamano_lista(l1):
  for i in l1:
    print (len(l1))
     
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Salidas
"""  
def informacion_lista():
  pass
#Retornar una l1 con los numero negativos  
"""
Entradas:
lista->list->l1
Salidas
lista->list->l1
"""  
def numeros_negativos(l1):
  aux=[]
  for i in l1:
    if(float(i)<0):
      aux.append(i)
  return aux    
#realizar una funcion que retorne la posicion de un elm que pasa por parametro
def posicion_elmemento(l1:list,elm:str):
  for i in l1:
    if(i==elm):
     p=l1.index(i)
     print (p)
     
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(l1,elm):
  l1.append(elm)
  return l1
#Realizar una funcion que cuente el numero de veces que se repite un elm  
def repetir(l1,elm):
  aux=[]
  for i in l1:
    aux.append(float(i))
  for i in aux:
    p=aux.count(elm)
  return p 

frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
l1_frutas=[]#Llenar las llistas con los datos del archivo frutas.txt
l1_numeros=[]#Llenar las listas con los datos del archivo numeros.txt
for i in frutas:
  l1_frutas.append(i)
for i in numeros:
  l1_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elmentos de la lista
"""
Entradas:
lista-->list-->l1
elemento->str-->elm
Salidas
lista-->l1
"""
def eliminar_un_caracter(l1,elm):
  auxilar=[]
  for i in l1:
    a=i.replace(elm,"")
    auxilar.append(a)
  return auxilar
 

#Realizar una funcion que retorne la copia de una lista que pasa por parametro 
"""
Entradas:
lista-list-->l1
Salidas
lista-list-->l1
"""
def copia_lista(l1):
  return lista.copy() 
#Realizar una funcion que retorne una lista de numeros enteros  
"""
Entradas:
lista-list-->l1
Salidas
lista-list-->l1
"""   
def numeros_enteros(l1):
  aux=[]
  aux_uno=[]
  for i in l1:
    aux.append(float(i))
  for i in aux:
    aux_uno.append(int(i))  
  return aux_uno

#Realiza una funcion que retorne una lista con los numeros pares
"""
Entradas:
lista-list-->l1
Salidas
lista-list-->l1
"""  
def numeros_pares(l1):
  aux=[]
  for i in l1:
    if(float(i)%2==0):
      aux.append(i)
  return aux    
#Realizar una funcion que elimine un elm de una lista
"""
Entradas:
lista-list-->l1
elmento-->str-->elm
Salidas
lista-list-->l1
"""  
def elimina_elemento_lista(l1,elm):
  lista.remove(elm)
  return lista


#Retorna una l1 con las palabras iniciales con la let que pasa por parametro  
"""
Entradas:
lista-list-->l1
letra-->str-->let
Salidas
lista-list-->l1
"""  
def palabras_por_letra (l1,elm):
  aux=[]
  for i in l1:
     if(i[0]==elm):
      aux.append(i)
  return aux


#Realizar una funcion que retorne el tamaño de una lista  
"""
Entradas:
lista->list->l1
Salidas
tamaño-->int->tm
"""   
def tm_l1(l1):
  for i in l1:
    print (len(l1))
     
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""

"""  
def informacion_l1():
  pass
#Retornar una lista con los numero negativos  
"""
Entradas:
lista->list->l1
Salidas
lista->list->l1
"""  
def numeros_negativos(l1):
  aux=[]
  for i in l1:
    if(float(i)<0):
      aux.append(i)
  return aux    
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
def posicion_elmento(l1:list,elm:str):
  for i in l1:
    if(i==elm):
     p=l1.index(i)
     print (p)
     
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(l1,elm):
  l1.append(elm)
  return l1
#Realizar una funcion que cuente el numero de veces que se repite un elemento
def repetir(l1,elm):
  aux=[]
  for i in l1:
    aux.append(float(i))
  for i in aux:
    p=aux.count(elm)
  return p 

if  _name_  ==  "_main_" :
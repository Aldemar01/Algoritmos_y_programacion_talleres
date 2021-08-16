"""
Entradas
capital-->float-->capi
Salidas
ganancia-->float-->gan
"""
capi=(float(input("Digite el capital a invertir: ")))
gan=(capi*0.02)
print("La ganancia es: "+ str(gan), "Ganancia con el capital: "+ str(gan+capi))

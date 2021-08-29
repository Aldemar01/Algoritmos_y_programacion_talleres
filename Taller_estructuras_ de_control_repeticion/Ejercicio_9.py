alcohol=0
gasolina=0
diesel=0
while(True):
    i=int(input())
    if(i == 4):
        break
    else:
        if (i == 1):
            alcohol = alcohol+1
        elif (i == 2):
            gasolina=gasolina+1
        elif (i == 3):
            diesel=diesel+1
        else:
            continue
print("MUITO OBRIGADO")
print("Alcool:",alcohol)
print("Gasolina:",gasolina)
print("Diesel:",diesel)
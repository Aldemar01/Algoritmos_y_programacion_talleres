line = input().split(" ") 
a,b,c = line
a=int(a)
b=int(b)
c=float(c)
line2 = input().split(" ")
a1,b1,c1 = line2
a1=int(a1)
b1=int(b1)
c1=float(c1)
pt= ((b*c))+(b1*c1)
print ("VALOR A PAGAR: R$ " "{:.2f}".format (pt))
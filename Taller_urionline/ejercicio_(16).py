input1= input().split(" ")
a,b =input1
a=float(a)
b=float(b)
input2= input().split(" ")
c,d =input2
c=float(c)
d= float(d)
dist= ((c-a)**2+(d-b)**2)**(1/2)
print("{:.4f}".format (dist))
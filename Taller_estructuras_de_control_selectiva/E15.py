
"""
Entradas
e
Edad-->ed-->int
Hemoglobina-->hmg-->int
salidas
sufre anemia
"""

ed = int (input (" Digite la ed del paciente: "))
hmg = int (input ('Digite la hmg del paciente: '))

if (ed>=0 and hmg >=0.13 or ed<=0,1 and hmg>=0.26):
    print ('no sufre anemia')
elif (ed>=0 and hmg <=0.13 or ed<=0,1 and hmg<=0.26):
    print ('sufre anemia')
if (ed>=0,1 and hmg >=0.10 or ed<=0,6 and hmg>=0.18):
    print ('no sufre anemia')
elif (ed>=0,1 and hmg <=0.10 or ed<=0,6 and hmg<=0.18):
    print ('sufre anemia')
if (ed>=0,6 and hmg >=0.11 or ed<=1 and hmg>=0.15):
    print ('no sufre anemia')
elif (ed>=0,6 and hmg <=0.11 or ed<=1 and hmg<=0.15):
    print ('sufre anemia')
if (ed>=1 and hmg >=0.115 or ed<=5 and hmg>=0.15):
    print ('no sufre anemia')
elif (ed>=1 and hmg <=0.115 or ed<=5 and hmg<=0.15):
    print ('sufre anemia')  
if (ed>=5 and hmg >=0.126 or ed<=10 and hmg>=0.155):
    print ('no sufre anemia')
elif (ed>=5 and hmg <=0.126 or ed<=10 and hmg<=0.155):
    print ('sufre anemia')
if (ed>=10 and hmg >=0.13 or ed<=15 and hmg>=0.155):
    print ('no sufre anemia')
elif (ed>=10 and hmg <=0.13 or ed<=15 and hmg<=0.155):
    print ('sufre anemia')  
        
print ()
#pruebas chiquitas para solucionar vergueos grandes
#primer vergueo
""" st = str(input("prueba: "))
print(st)
z = st.upper()
y = st.lower()
print(z)
print(y)
print(dir(st))
print(st.__add__("b")) """

#segundo vergueo
"""class prueba(object):
    def __init__(self):
        self.b=True
        self.list = ["a","b"]
    def setboo(self, valor):
        self.b = valor
    def getboo(self):
        return str(self.b)
    def setL(self, valor):
        self.list =valor
    def getL(self):
        return self.list


a = prueba()
print(a.getL())
b=["z","x"]
a.setL(b)
print(a.getL()) """

#tercer duda
""" s = str(input("ingreso: "))
a = s.split(">")
print(len(a))
print(a)
b = a[0].split(" ")
c = a[1].split(" ")
print(len(b))
print(len(c))
print(b)
print(c)
df=''
print(df.isupper())
print(df.islower()) """
""" print(b[0])
print(c[1])
print(c[2])
print(b[0].isupper())
print(c[1].islower())
print(c[2].isupper()) """

#cuarta duda
""" nombre = input("Ingrese el nombre del archivo para generar el AFD: ")
name = nombre.split('.')
print(name[0])
archivo = open(nombre, 'r')
tela = archivo.read()
archivo.close()
input(tela) 
 """
#quinta
#a=input("aaa: ")
#print(a.islower())

##sexta
""" a = True
if a == True:
    print("es verdadero")
else:
    print("es falso") """
#septima

""" a = "a"
b=", b"
c= a.__add__(b+", c")
print(c)
num=""
fin =""
for a in range(5):
    fin+=str(a)
print(fin)
 """

 
#generando un hermoso pdf :3
"""from reportlab.pdfgen import canvas
c = canvas.Canvas("prueba2.pdf")
                #x,y,texto
a="hol"                
c.drawString(100,750,"hola desde pdf")
path= "C:\\Users\\almxo\\Downloads\\aa.jpg"
c.drawImage(path,275,275,125,100)
c.drawString(100,730,a+"a")
c.save()"""

# graphiz
#import subprocess
"""#subprocess.call('dot C:\\Users\\almxo\\Desktop\\pure.dot -Tpng -o C:\\Users\\almxo\\Desktop\\image.png ')
try:
    a=2
    print(a+"a")
except:
    print("ocurrio algo")
"""
##
"""import os
archivo = open("C:\\Users\\almxo\\Desktop\\filename.txt", "w")
archivo.write("Primera línea\n")
archivo.write("Segunda línea")
archivo.close()"""
a=["a","b"]
b=["c","d","e"]
if a.__len__()==b.__len__():
    print("misma longitud")

import os
from io import open 
import codecs
from Armeria import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import subprocess

class Menu():
    def __init__(self):
        self.boveda = []
        valor ="teniaquehacerlo"
        teniaque = Aefede(valor)
        self.boveda.append(teniaque)        
        #self.GRS = []

    def Iniciar(self):
        self.clrsrc()
        print("Lenguajes Formales de programación")
        print("Sección B")
        print("Luis Amilcar Morales Xón \n201701059")
        input("\nPresione Enter para continuar")
        #self.clrsrc()
        try:
            self.Menu()     
        except:
            self.Menu()
##menu primer grado
    def Menu(self):
        salida = True		
        while salida:
            self.clrsrc()
            print ("********** Menu **********\n")
            print("1- Modulo AFD")
            print("2- Modulo de Gramática Regulares")
            print("3- Acerda de")
            print("4- Salir\n")
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                self.clrsrc()
                self.SubAFD()                
            elif opcion == 2:
                self.clrsrc()
                self.SubGR()                
            elif opcion == 3:
                self.clrsrc()
                self.AcerdaDe()
            elif opcion == 4:
                self.clrsrc()                        
                salida = False
            else:
                self.clrsrc()
                input("Ingrese una opción valida")

##Menu de segundo grado

###pinche menu de aefedes
    def SubAFD(self):
        self.clrsrc()
        salida1 = True
        while salida1:            
            print("********** Menú de AFD **********\n")
            print('1- Crear AFD')
            print('2- Cargar archivo')
            print('3- Evaluar cadena')
            print('4- Guardar AFD en archivo')
            print('5- Generar reporte AFD')
            print('6- Generar gramática regular')
            print('7- Menu principal\n')
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                #crear afd
                self.clrsrc()
                flagAFD = 0
                name = str(input("Ingrese el nombre del AFD: "))
                for a in range(self.boveda):
                    if name == self.boveda[a].getName():
                       flagAFD+=1
                if flagAFD!= 0:
                    input("No puede haber dos AFD's con el mismo nombre, intentelo otra vez.")
                else:
                    nuevoAFD = Aefede(name)
                    self.boveda.append(nuevoAFD)
                    self.IngresarEstados(name)
                    self.IngresarAlfabeto(name)
                    self.EstadoInicial(name)
                    self.Aceptation(name)
                    self.AddTransiciones(name)
                self.clrsrc()
            elif opcion == 2:
                self.clrsrc()
                self.cargaAFD()
                self.clrsrc()
            elif opcion == 3:
                input("Evaluar cadena")                            
            elif opcion == 4:
                input("Guardar en archivo")
            elif opcion == 5:
                input("generar reporte")
            elif opcion == 6:
                input("generar gramatica")
            elif opcion == 7:
                salida1 = False                
            else:
                self.clrsrc()
                input("Ingrese una opción valida")

    #pinche menu de gramaticas
    def SubGR(self):
        self.clrsrc()
        salida2 = True
        while salida2:            
            print("********** Menú de Gramáticas **********\n")
            print('1- Crear gramática')
            print('2- Cargar archivo')
            print('3- Evaluar cadena')
            print('4- Eliminar recursividad por la izquierda')
            print('5- Guardar gramática en archivo')
            print('6- Generar reporte gramática regular')
            print('7- Menu principal\n')
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                #Crear gramatica
                self.clrsrc()
                flagGR = 0
                name = str(input("Ingrese el nombre de la gramática: "))
                for a in range(self.boveda):
                    if name == self.boveda[a].getName():
                       flagGR+=1
                if flagGR!= 0:
                    input("No puede haber dos gramáticas con el mismo nombre, intentelo otra vez.")
                else:
                    nuevaGR = Gramatica(name)
                    self.boveda.append(nuevaGR)
                    self.IngresarNT(name)
                self.clrsrc()

            elif opcion == 2:
                input("Cargando archivo")
            elif opcion == 3:
                input("Evaluar cadena")                            
            elif opcion == 4:
                input("Guardar en archivo")
            elif opcion == 5:
                input("generar reporte")
            elif opcion == 6:
                input("generar gramatica")
            elif opcion == 7:
                salida2 = False                
            else:
                self.clrsrc()
                input("Ingrese una opción valida")            
    
    ##pinche menu evaluar cadenas
    def SubEChain(self):
        name = input('Ingrese el nombre de la Gramatica: ')
        for i in range(len(self.boveda)):
            if name == str(self.boveda[i]):
                saldo = True
                while saldo:
                    self.clrsrc()
                    print("********** Menú de Evaluar Cadenas **********\n")
                    print('1- Solo validar')
                    print('2- Ruta en AFD')
                    print('3- Expandir con gramatica')
                    print('4- Ayuda')
                    print('5- Menu principal\n')
                    opcion = int(input('Ingrese una opción: '))
                    if opcion == 1:
                        try:
                            input("validando cadena")
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 2:
                        try:
                            input("ruta en afd")
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 3:
                        try:
                            input("ruta en gramatica")
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 4:
                        self.clrsrc()
                        self.Help()
                    elif opcion == 5:
                        saldo = False
                        try:
                            self.Menu()
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    else:
                        self.clrsrc()
                        input("Ingrese una opción valida")
            else:
                input("Eso no funcionó, intentelo otra vez. \nEscribe bien el nombre.")
    

    
    #Pinche menu cargar archivo    

    def generarAFD(self,nome):
        for a in range(len(self.boveda)):
            if self.boveda[a].getName()==nome and self.boveda[a].getTipo()=="Gramatica":
                nuevoAFD = Aefede(nome)
                predetermindado = Estado("PR")
                predetermindado.setAcepta(True)
                nuevoAFD.setPrede(predetermindado)
                #conviertiendo no terminales a estados
                for i in range(len(self.boveda[a].getNoTerms())):
                    nuevoEstado=Estado(self.boveda[a].getNoTerms()[i].getName())
                    nuevoEstado.setAcepta(self.boveda[a].getNoTerms()[i].getEpsilon())
                    nuevoEstado.setInicio(self.boveda[a].getNoTerms()[i].getInicio())
                    nuevoEstado.setSalidas(self.boveda[a].getNoTerms()[i].getSalidas())
                    nuevoAFD.getEstados().append(nuevoEstado)
                #terminales pasan a ser el alfabeto
                nuevoAFD.setAlfabeto(self.boveda[a].getTerminales())
                #producciones a transiciones :"v
                for j in range(len(self.boveda[a].getProducciones())):
                    if self.boveda[a].getProducciones()[j].getTerminal()!="epsilon":
                        nuevoTrance= Transicion(self.boveda[a].getProducciones()[j].gettInicial(),self.boveda[a].getProducciones()[j].gettFinal(),self.boveda[a].getProducciones()[j].getTerminal())
                        nuevoAFD.getTransiciones().append(nuevoTrance)
                self.boveda.append(nuevoAFD)
    
    def generarGR(self,nome):
        for a in range(len(self.boveda)):
            if self.boveda[a].getName()==nome and self.boveda[a].getTipo()=="AFD":
                nuevaGR= Gramatica(nome)
                predetermindado = noTerminal("PR")
                predetermindado.setEpsilon(True)
                nuevaGR.setPrede(predetermindado)
                #conviertiendo estados a no terminales
                for i in range(len(self.boveda[a].getEstados())):
                    nuevoNT=noTerminal(self.boveda[a].getEstados()[i].getNameE())
                    nuevoNT.setEpsilon(self.boveda[a].getEstados()[i].getAcepta())
                    nuevoNT.setInicio(self.boveda[a].getEstados()[i].getInicio())
                    nuevoNT.setSalidas(self.boveda[a].getEstados()[i].getSalidas())
                    nuevaGR.getNoTerms().append(nuevoNT)
                #alfabeto pasa a ser terminales
                nuevaGR.setTerminales(self.boveda[a].getAlfabeto())
                #transiciones a producciones; lo vi dificl pero solo era ajustar unas ondas
                for j in range(len(self.boveda[a].getTransiciones())):
                    nuevaProd = Produccion(self.boveda[a].getTransiciones()[j].geteInicial(),self.boveda[a].getTransiciones()[j].geteFinal(),self.boveda[a].getTransiciones()[j].getEntrada())
                    nuevaGR.getProducciones().append(nuevaProd)
                self.boveda.append(nuevaGR)

    def escribirAFD(self,nombre, nome):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')        
        archivo = open(path_desktop+"\\"+nombre+".afd", 'w')
        #for para recorrer lista general
        
        for i in range(len(self.boveda)):
            if self.boveda[i].getName()==nome and self.boveda[i].getTipo()=="AFD":
                #for para recorrer la lista de transicion del afd actual
                for j in range(len(self.boveda[i].getTransiciones())):
                    boolean1 = ""
                    boolean2 = ""
                    #for para recorrer lista de estados del afd actual
                    for a in range(len(self.boveda[i].getEstados())):                        
                        if self.boveda[i].getTransiciones()[j].geteInicial()==self.boveda[i].getEstados()[a].getNameE():
                            if self.boveda[i].getEstados()[a].getAcepta() == True:
                                boolean1 = "true"
                            else:
                                boolean1 = "false"
                        if self.boveda[i].getTransiciones()[j].geteFinal()==self.boveda[i].getEstados()[a].getNameE():
                            if self.boveda[i].getEstados()[a].getAcepta() == True:
                                boolean2 = "true"
                            else:
                                boolean2 = "false"
                        elif self.boveda[i].getTransiciones()[j].geteFinal()=="PR":
                            boolean2 = "true"
                    archivo.writelines(self.boveda[i].getTransiciones()[j].geteInicial()+","+self.boveda[i].getTransiciones()[j].geteFinal()+","+self.boveda[i].getTransiciones()[j].getEntrada()+";"+boolean1+","+boolean2+"\n")
        archivo.close()

    def escribirGR(self,nombre, nome):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        archivo = open(path_desktop+"\\"+nombre+".gre", 'w')
        for i in range(len(self.boveda)):
            if self.boveda[i].getName() == nome and self.boveda[i].getTipo()=="Gramatica":
                for j in range(len(self.boveda[i].getProducciones())):                    
                    archivo.writelines(self.boveda[i].getProducciones()[j].gettInicial()+" > "+self.boveda[i].getProducciones()[j].getTerminal()+" "+self.boveda[i].getProducciones()[j].gettFinal()+"\n")
        archivo.close()
    #wwwwwwwwwwwwwwwwwwwwwwww
    #eeeeeeeeeeeeeeeeeeeeeeee
    ####alllllltoooooo fin menu guardar
    
    #Pinche menú culero 
    def Reporte(self):
        name = input('Ingrese el nombre del AFD o la Gramatica: ')
        flag=0
        for i in range(len(self.boveda)):
            if name == str(self.boveda[i].getName()):
                flag+=1
        if flag!=0:
            salida =True
            while salida:
                self.clrsrc()
                print("********** Menú de Reportes **********\n")
                print('1- Ver detalle')
                print('2- Generar reporte')
                print('3- Ayuda')
                print('4- Menú Principal\n')
                opcion = int(input('Ingrese una opción: '))
                if opcion == 1:
                    self.clrsrc()
                    try:
                        self.verDetalle(name)
                    except:
                        print("Parece que tenemos problemas, se va a estabilizar.")
                elif opcion == 2:
                    self.clrsrc()
                    
                    self.generarReporte(name)
                    
                elif opcion == 3:
                    self.clrsrc()
                    self.Help()
                elif opcion == 4:
                    salida = False
                    try:
                        self.Menu()
                    except:
                        print("Parece que tenemos problemas, se va a estabilizar.")
                else:
                    self.clrsrc()
                    input("Ingrese una opción valida")
        else:
            input("Eso no funcionó, intentelo otra vez. \nEscribe bien el nombre.")

    def verDetalle(self,indice):
        flagAFD = 0
        flagGR = 0
        for a in range(len(self.boveda)):
            if indice == self.boveda[a].getName() and self.boveda[a].getTipo()=="AFD":
               flagAFD+=1
            if indice == self.boveda[a].getName() and self.boveda[a].getTipo()=="Gramatica": 
                flagGR+=1
            #ninguno existe
        if flagAFD==0 and flagGR == 0:
            input("\nParece que el elemento que busca no existe en memoria, Intentelo otra vez.")
            #gramatica no existe 
            #afd existe
        elif flagAFD!=0 and flagGR == 0:
            print("\nHemos comprobado que el elemento solo existe como AFD. Pero se puede generar la gramatica si es lo que quiere.\n")
            tipo = input("Ingrese \"AFD\" para consultar el automata o \"GR\" para la gramatica: ")            
            if tipo=="AFD":
                self.detalleAFD(indice)
            elif tipo=="GR":
                self.generarGR(indice)
                self.detalleGR(indice)
            #gramatica existe
            #afd no existe
        elif flagAFD==0 and flagGR!=0:
            print("\nHemos comprobado que el elemento solo existe como Gramatica. Pero se puede generar el AFD si es lo que quiere.\n")
            tipo = input("Ingrese \"AFD\" para consultar el automata o \"GR\" para la gramatica: ")            
            if tipo=="AFD":
                self.generarAFD(indice)
                self.detalleAFD(indice)
            elif tipo=="GR":
                self.detalleGR(indice)
        elif flagAFD!=0 and flagGR!=0:
            print("\nHemos comprobado que el elemento existe como Gramatica y como AFD.\n")
            tipo = input("Ingrese \"AFD\" para consultar el automata o \"GR\" para la gramatica: ")            
            if tipo == "AFD":
                self.detalleAFD(indice)
            elif tipo == "GR":
                self.detalleGR(indice)
    
    def generarReporte(self,indice):
        flagAFD = 0
        flagGR = 0
        for a in range(len(self.boveda)):
            if indice == self.boveda[a].getName() and self.boveda[a].getTipo()=="AFD":
               flagAFD+=1
            if indice == self.boveda[a].getName() and self.boveda[a].getTipo()=="Gramatica": 
                flagGR+=1
            #ninguno existe
        if flagAFD==0 and flagGR == 0:
            input("\nParece que el elemento que busca no existe en memoria, Intentelo otra vez.")
            #gramatica no existe 
            #afd existe
        elif flagAFD!=0 and flagGR == 0:                                                
            #generar gramatica
            
            self.generarGR(indice)    
            self.clrsrc()        
            self.generarHermosoPFD(indice)
            
        elif flagAFD==0 and flagGR!=0:
            #Generar Afd            
            
            self.generarAFD(indice)
            self.clrsrc()
            self.generarHermosoPFD(indice)            
        elif flagAFD!=0 and flagGR!=0:
            #solo generar pdf
            self.generarHermosoPFD(indice)            
    
    def detalleAFD(self,nome):
        self.clrsrc()
        for a in range(len(self.boveda)):
            if nome ==self.boveda[a].getName() and self.boveda[a].getTipo()=="AFD":
                #Alfabeto
                print("\nNombre del AFD: " +self.boveda[a].getName())
                print("\nAlfabeto:")
                print(self.boveda[a].getAlfabeto())                            
                #estados
                print("Estados:")
                listaEstados=[]
                for p in range(len(self.boveda[a].getEstados())):
                    listaEstados.append(self.boveda[a].getEstados()[p].getNameE())
                print(listaEstados)
                #estado inicial
                start=""
                for i in range(len(self.boveda[a].getEstados())):
                    if self.boveda[a].getEstados()[i].getInicio()==True:
                        start=self.boveda[a].getEstados()[i].getNameE()
                print("Estado inicial: "+start)
                #estados de aceptación.
                dijosi=""                
                for j in range(len(self.boveda[a].getEstados())):
                    if self.boveda[a].getEstados()[j].getAcepta()==True:
                        dijosi+=self.boveda[a].getEstados()[j].getNameE()+","
                        
                print("Estados de aceptación: ["+dijosi+"]")
                #Transiciones
                print("Transiciones:")
                for q in range(len(self.boveda[a].getTransiciones())):
                    print(self.boveda[a].getTransiciones()[q].geteInicial()+","+self.boveda[a].getTransiciones()[q].geteFinal()+";"+self.boveda[a].getTransiciones()[q].getEntrada())
                input("Fin del reporte, Presione Enter para continuar.")

    def detalleGR(self, nome):
        self.clrsrc()
        for a in range(len(self.boveda)):
            if nome ==self.boveda[a].getName() and self.boveda[a].getTipo()=="Gramatica":
                #Noterminales
                print("\nNombre de la Gramatica: " +self.boveda[a].getName())
                print("\nNo terminales:")
                listaNoTerminales=[]
                for p in range(len(self.boveda[a].getNoTerms())):
                    listaNoTerminales.append(self.boveda[a].getNoTerms()[p].getName())
                print(listaNoTerminales)
                #Terminales
                print("Terminales:")                                    
                print(self.boveda[a].getTerminales())
                #Inicio
                start=""
                for i in range(len(self.boveda[a].getNoTerms())):
                    if self.boveda[a].getNoTerms()[i].getInicio()==True:
                        start=self.boveda[a].getNoTerms()[i].getName()
                print("Estado inicial: "+start)
                #Producciones
                print("Producciones:")
                for z in range(len(self.boveda[a].getProducciones())):
                    print(self.boveda[a].getProducciones()[z].gettInicial()+" > "+self.boveda[a].getProducciones()[z].getTerminal()+" "+self.boveda[a].getProducciones()[z].gettFinal())
                input("Fin del reporte, Presione Enter para continuar.")                  

    def generarHermosoPFD(self, nome):
        nombre = nome+".pdf"
        c = canvas.Canvas(nombre)
        #parte donde agrego los detalles
        c.setFontSize(16)
        c.drawString(225,775,nome)        
        c.drawString(75,730, "Gramática regular.")  
        c.drawString(345,730, "Automata finito determinista.")      
        c.setFont('Helvetica', 11)
        for a in range(len(self.boveda)):
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()=="Gramatica":                
                nombre= "Nombre: "+self.boveda[a].getName()
                c.drawString(75,715,nombre)
                #añadiendo terminales
                terminal=""
                resultado=""
                for i in range(len(self.boveda[a].getTerminales())):
                    terminal+=self.boveda[a].getTerminales()[i]+", "
                
                resultado="Terminales: "+terminal
                c.drawString(75,700,resultado)
                #añadiendo no terminales
                Nt=""
                resu=""
                for j in range(len(self.boveda[a].getNoTerms())):
                    Nt+=self.boveda[a].getNoTerms()[j].getName()+", "
                resu="No Terminales: "+Nt
                c.drawString(75,685,resu)
                #añadiendo inicio
                starto=""
                stuart=""
                for k in range(len(self.boveda[a].getNoTerms())):
                    if self.boveda[a].getNoTerms()[k].getInicio()==True:
                        starto=self.boveda[a].getNoTerms()[k].getName()
                stuart= "No terminal inicial: "+starto
                c.drawString(75,670,stuart)
                #añadiendo producciones
                c.drawString(75,655,"Producciones:")
                line = int(640)
                prado=""
                for l in range(len(self.boveda[a].getProducciones())):
                    line-=15
                    prado=self.boveda[a].getProducciones()[l].gettInicial()+" > "+self.boveda[a].getProducciones()[l].getTerminal()+" "+self.boveda[a].getProducciones()[l].gettFinal()
                    c.drawString(75,line,prado)
                ##parte del automata
                #c.drawString(345,730, "Automata finito determinista.")
            elif nome == self.boveda[a].getName() and self.boveda[a].getTipo()=="AFD":
                c.drawString(345,715,"Nombre: "+self.boveda[a].getName())
                #alfabeto
                alfa=""
                for i in range(len(self.boveda[a].getAlfabeto())):
                    alfa+=self.boveda[a].getAlfabeto()[i]+", "
                c.drawString(345,700,"Alfabeto:"+alfa)
                #estados
                estadio=""
                for j in range(len(self.boveda[a].getEstados())):
                    estadio+=self.boveda[a].getEstados()[j].getNameE()+", "
                c.drawString(345,685,"Estados: "+estadio)
                #inicial
                estarto=""
                for k in range(len(self.boveda[a].getEstados())):
                    if self.boveda[a].getEstados()[k].getInicio()==True:
                        estarto=self.boveda[a].getEstados()[k].getNameE()
                c.drawString(345,670,"Estado inicial: "+estarto)
                #estados de aceptación
                estufa=""
                for l in range(len(self.boveda[a].getEstados())):
                    if self.boveda[a].getEstados()[l].getAcepta()==True:
                        estufa+=self.boveda[a].getEstados()[l].getNameE()+", "
                c.drawString(345,655,"Estados de aceptación: "+estufa)
                #grafica
                self.generarDot(nome)
                "C:\\Users\\almxo\\Desktop\\"+nome+".dot"
                subprocess.call("dot C:\\Users\\almxo\\Desktop\\"+nome+".dot -Tpng -o C:\\Users\\almxo\\Desktop\\"+nome+".png")
                pato="C:\\Users\\almxo\\Desktop\\"+nome+".png"
                c.drawImage(pato,190,530,300,100)                
                
        c.save()
    
    def generarDot(self, nome):
        archivo = open("C:\\Users\\almxo\\Desktop\\"+nome+".dot", 'w')
        archivo.write("digraph A {\n")
        archivo.write("rankdir = LR;\n")
        archivo.write("EMPTY [style=invis]\n")
        archivo.write("EMPTY [shape=point]\n")
        for a in range(len(self.boveda)):
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()=="AFD":
                #agregando estados al dot
                for i in range(len(self.boveda[a].getEstados())):
                    if self.boveda[a].getEstados()[i].getAcepta()==True:
                        archivo.write("node [shape=doublecircle,style=filled] "+self.boveda[a].getEstados()[i].getNameE()+"\n")
                    else:
                        archivo.write("node [shape=circle,style=filled] "+self.boveda[a].getEstados()[i].getNameE()+"\n")
                #agregando transiciones
                eInicial=""
                for h in range(len(self.boveda[a].getEstados())):
                    if self.boveda[a].getEstados()[h].getInicio()==True:
                        eInicial=self.boveda[a].getEstados()[h].getNameE()
                #EMPTY -> INCIO [label =""];
                archivo.write("EMPTY"+" -> "+eInicial+" [label=\" "+" \"];\n")
                for j in range(len(self.boveda[a].getTransiciones())):
                    
                    archivo.write(self.boveda[a].getTransiciones()[j].geteInicial()+" -> "+self.boveda[a].getTransiciones()[j].geteFinal()+" [label=\""+self.boveda[a].getTransiciones()[j].getEntrada()+" \"];\n")
                archivo.write("}")
        archivo.close()     

#ddddddddddddddddddddddddddddd
#222222222222222222222222222222
#fin menu culero de reportes                    
    def clrsrc(self):
        os.system("cls")

    def AcerdaDe(self):
        print("Lenguajes Formales de Programación \nAuxiliar: Danilo Urias \nSección: B")
        input("Pulsa ENTER para continuar")
    
    #santo vergueo para un pinche estado
    def IngresarEstados(self, nome):
        print("AFD llamado: "+nome+"\nEscriba >>salir<< para dejar de ingresar estados")
        salida = True
        while salida:   
            estado = str(input("\nIngrese un estado para el AFD: "))            
            if estado != "salir":                
                self.CrearEstados(nome,estado)
            else:
                salida = False

    def CrearEstados(self, nome, estado):
        state = Estado(estado)
                #print("acabamos de crear el estado")
        for a in range(len(self.boveda)):
                    #print("estamos verificando afds")
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()== "AFD":
                        #print("encontramos el afd")
                if self.boveda[a].getEstados():
                    flag = 0
                    for i in range(len(self.boveda[a].getEstados())):
                                #print("verificando estados  del afd")
                        if estado == self.boveda[a].getEstados()[i].getNameE():
                            flag+=1

                    if flag == 0:
                        self.boveda[a].getEstados().append(state)
                    else:
                        print("El estado ya existe, no puede haber dos estados con el mismo nombre.")
                                #estesi[a].getEstados().append(state)
                else:                    
                    self.boveda[a].getEstados().append(state)
                            #estesi[a].getEstados().append(state)
    #vergueo de alfabeto
    def IngresarAlfabeto(self, nome):
        print("AFD llamado: "+nome+"\nEscriba >>salir<< para dejar de ingresar elementos del alfabeto")
        salida = True
        while salida:   
            dato = str(input("\nIngrese un elemento del alfabeto para el AFD: "))
            alfa = dato.lower()
            if dato != "salir":
                self.CrearAlfabeto(nome,alfa)
            else:
                salida = False

    def CrearAlfabeto(self, nome, alfa):
        for a in range(len(self.boveda)):
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()== "AFD":
                #viendo si no ingresamos un alfabeto que ya está como estado
                bandera = 0
                for k in range(len(self.boveda[a].getEstados())):
                    if alfa != self.boveda[a].getEstados[k].getNameE():
                        bandera+=0
                if bandera==0:
                    print("podemos ingresar el alfabeto")
                    if self.boveda[a].getAlfabeto():    
                        flag = 0                                                                                
                        for i in range(len(self.boveda[a].getAlfabeto())):
                            if alfa == self.boveda[a].getAlfabeto()[i]:                                    
                                flag+=1

                        if flag == 0:
                            self.boveda[a].getAlfabeto().append(alfa)
                        else:
                            print("El caracter ya existe en el alfabeto.")
                    else:
                        self.boveda[a].getAlfabeto().append(alfa)
                else:
                    input("El caracter que se quiere agregar como alfabeto ya está como un estado.\nNo se puede realizar la operacion.")
                
    #vergueo del estado inicial
    def EstadoInicial(self, nome):
        print("AFD llamado: "+nome+"\n")
        dato = str(input("Ingrese un estado existente para declararlo como estado inicial del AFD: "))
        self.AsignarEstadoInicial(nome,dato)
        
    def AsignarEstadoInicial(self, nome, dato):
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()== "AFD":
                if self.boveda[i].getEstados():                    
                    #busco el nuevo estado
                    for b in range(len(self.boveda[i].getEstados())):
                        if self.boveda[i].getEstados()[b].getNameE()==dato:                            
                            #borro el estado inicial anterior
                            for a in range(len(self.boveda[i].getEstados())):
                                #print("cambiando estados")
                                self.boveda[i].getEstados()[a].setInicio(False)                            
                            self.boveda[i].getEstados()[b].setInicio(True)                                                        
                else:
                    input("El AFD al que intenta asignar un estado inicial no cuenta con ningun estado todavia.")

    #vergueo de los estados de aceptación
    def Aceptation(self, nome):
        print("AFD llamado: "+nome+"\nEscriba >>salir<< para dejar de ingresar estados de aceptación.")
        salida = True
        while salida:   
            dato = str(input("\nIngrese un estado existente para convertirla en aceptación para el AFD: "))            
            if dato != "salir":
                self.Acetona(nome,dato)
            else:
                salida = False

    def Acetona(self,nome,dato):
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()== "AFD":                        
                if self.boveda[i].getEstados():                                                
                    for b in range(len(self.boveda[i].getEstados())):
                        if self.boveda[i].getEstados()[b].getNameE()==dato:                                                                
                            self.boveda[i].getEstados()[b].setAcepta(True)                         
                else:
                    print("El AFD al que intenta asignar estados de aceptacion no cuenta con ningun estado todavia.")

    def AcetonaInverso(self,nome,dato):
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()== "AFD":                        
                if self.boveda[i].getEstados():                                                
                    for b in range(len(self.boveda[i].getEstados())):
                        if self.boveda[i].getEstados()[b].getNameE()==dato:                                                                
                            self.boveda[i].getEstados()[b].setAcepta(False)                                                        

    #otro vergueo mamalon con las transiciones        
    #ingreso de las transiciones
    def AddTransiciones(self, nome):        
        print("AFD llamado: "+nome+"\nIngresando transiciones. Escriba >>salir<< para detenerse.")
        print("Ejemplo de la sintaxis de ingreso: \"A,0;B\"")
        salida = True
        while salida:        
            trans = input("\nIngrese una transición: ")
            if trans != "salir":
                #try:
                self.Transiciones(nome,trans)                
                #except:
                    #print("Parece que tenemos problemas, se va a estabilizar.")
            else:
                salida = False

    def Transiciones(self, nome, trans):
        frag = trans.split(';')
                #  0  , 1
        #Frag = ["A,1","B"]
        #estados = ["A","1"]
        estados = frag[0].split(',')
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()=="AFD":
                flag1=0
                flag2=0
                flag3=0
                banderita=0
                inicial = None
                final = None
                #Validando terminal involucrado en la transición.
                for c in range(len(self.boveda[i].getAlfabeto())):
                    if estados[1] == self.boveda[i].getAlfabeto()[c]:
                        flag3+=1
                                #input("terminal")

                #validando estado inicial y que no haya mas de una transición con la misma terminal
                for a in range(len(self.boveda[i].getEstados())):
                    if estados[0] == self.boveda[i].getEstados()[a].getNameE():
                        flag1+=1
                        inicial = self.boveda[i].getEstados()[a]
                        if self.boveda[i].getEstados()[a].getSalidas():

                            for k in range(len(self.boveda[i].getEstados()[a].getSalidas())):
                                if frag[1]==self.boveda[i].getEstados()[a].getSalidas()[k]:
                                    banderita+=1                                        
                            if banderita == 0:
                                self.boveda[i].getEstados()[a].getSalidas().append(frag[1])
                        else:
                            self.boveda[i].getEstados()[a].getSalidas().append(frag[1])
                                #input("inicio")
                #validando estado final
                for b in range(len(self.boveda[i].getEstados())):
                    if frag[1]== self.boveda[i].getEstados()[b].getNameE():
                        flag2+=1
                        final = self.boveda[i].getEstados()[b]
                                #input("final")

                if flag1!=0 and flag2!=0 and flag3!=0:
                    if banderita==0:                            
                        trancy = Transicion(inicial, final, frag[1])
                        self.boveda[i].getTransiciones().append(trancy)
                    else:
                        print("Ésta acción no se completó.\nUsted está tratando de crear un Automata Finito NO Determinista o Está ingresando una transición que ya existe.")
                else:
                    print("Almenos un estado que está involucrado en ésta transición no existe en la lista de estados de este AFD.\nO bien el terminal involucrado no existe en el alfabeto del AFD")
##gramaticas
##Gramaticas
##Gramaticas
#copia del santo vergueo para un pinche estado y modificado para un no terminal
    def IngresarNT(self, nome):
        print("Gramática llamada: "+nome+"\nEscriba >>salir<< para dejar de ingresar No Terminales")
        salida = True
        while salida:   
            NT = str(input("\nIngrese un No terminal para la Gramática: "))            
            if NT != "salir":                
                self.CrearNoTerminal(nome,NT)
            else:
                salida = False                

    def CrearNoTerminal(self,nome,NT):
        terminator = noTerminal(NT)
        for a in range(len(self.boveda)):                    
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo() == "Gramatica":                        
                if self.boveda[a].getNoTerms():    
                    flag = 0                                                                                
                    for i in range(len(self.boveda[a].getNoTerms())):                                
                        if NT == self.boveda[a].getNoTerms()[i].getName():                                    
                            flag+=1

                    if flag == 0:
                        self.boveda[a].getNoTerms().append(terminator)
                                #print("agregado")
                    else:
                        print("El No Terminal ya existe, no puede haber dos No Terminales con el mismo nombre.")                                
                else:                    
                    self.boveda[a].getNoTerms().append(terminator)
                            #print("agredado 1")
    #copia del vergueo de alfabeto modificado para terminales
    def IngresarTerminales(self, nome):
        print("Gramatica llamada: "+nome+"\nEscriba >>salir<< para dejar de ingresar terminales.")
        salida = True
        while salida:   
            dato = str(input("\nIngrese un terminal para la Gramatica: "))
            zona4 = dato.lower()
            if dato != "salir":
                self.CrearTerminales(nome,zona4)
            else:
                salida = False
    def CrearTerminales(self,nome,zona4):
        for a in range(len(self.boveda)):
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()== "Gramatica":
                #viendo si podemos agregar el terminal
                bandera = 0
                for k in range(len(self.boveda[a].getNoTerms())):
                    if zona4 == self.boveda[a].getNoTerms()[k].getName():
                        bandera+=0
                if bandera == 0:
                    #podemos agregar la terminal
                    if self.boveda[a].getTerminales():    
                        flag = 0                                                                                
                        for i in range(len(self.boveda[a].getTerminales())):
                            if zona4 == self.boveda[a].getTerminales()[i]:                                    
                                flag+=1

                        if flag == 0:
                            self.boveda[a].getTerminales().append(zona4)
                        else:
                            print("El Terminal ya existe para la Gramatica.")
                    else:
                        self.boveda[a].getTerminales().append(zona4)                    
                    
                else:
                    input("El terminal que se quiere agregar a la lista ya está como un No Terminal.\nNo se puede realizar la operacion.")                    
    
    #Copia del vergueo del estado inicial para gramaticas
    def NoTerminalInicial(self, nome):
        print("Gramatica llamada: "+nome+"\n")
        dato = str(input("Ingrese un No Terminal existente para declararlo como inicial: "))
        self.AsignarNoTerminalInicial(nome,dato)
        
    def AsignarNoTerminalInicial(self,nome,dato):
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()== "Gramatica":
                if self.boveda[i].getNoTerms():                                        
                    for b in range(len(self.boveda[i].getNoTerms())):
                        if self.boveda[i].getNoTerms()[b].getName()==dato:                            
                            for a in range(len(self.boveda[i].getNoTerms())):
                                self.boveda[i].getNoTerms()[a].setInicio(False)

                            self.boveda[i].getNoTerms()[b].setInicio(True)                                                        
                else:
                    input("El AFD al que intenta asignar un estado inicial no cuenta con ningun estado todavia.")
    
    #Ingreso de producciones
    #vamo a ver
    def Produu(self, nome):
        self.clrsrc()
        print("Gramatica llamada: "+nome+"\nIngresando Producciones. Escriba >>salir<< para detenerse.")
        print("Ejemplo de la sintaxis de ingreso: \"A > a B\"")
        salida = True
        while salida:        
            trans = input("\nIngrese una producción: ")
            if trans != "salir":
                self.CrearProducciones(nome,trans)
            else:
                salida = False
    
    def CrearProducciones(self,nome,trans):
        frag = trans.split('>')
        NT1 = frag[0].split(' ')
        NT2 = frag[1].split(' ')
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()=="Gramatica":
                flag1=0
                flag2=0
                flag3=0
                banderita = 0
                inicial = None
                final = None                        
                if len(NT2)==3:
                            #print("hay recusividad")

                    if NT2[1].isupper()==True:
                        self.boveda[i].setIzquierda(True)
                                #print("Recursivo por la izquierda")
                        for a in range(len(self.boveda[i].getNoTerms())):
                            if NT1[0]== self.boveda[i].getNoTerms()[a].getName():
                                flag1+=1
                                inicial = self.boveda[i].getNoTerms()[a]
#                                        input("inicio")

                        for b in range(len(self.boveda[i].getNoTerms())):
                            if NT2[1]== self.boveda[i].getNoTerms()[b].getName():
                                flag2+=1
                                final = self.boveda[i].getNoTerms()[b]
 #                                       input("final")

                        for c in range(len(self.boveda[i].getTerminales())):
                            if NT2[2] == self.boveda[i].getTerminales()[c]:
                                flag3+=1
  #                                      input("terminal")

                        if flag1!=0 and flag2!=0 and flag3!=0:                            
                            proud = Produccion(inicial, final, NT2[2])
                            self.boveda[i].getProducciones().append(proud)
                        else:
                            print("Almenos un No terminal que está involucrado en ésta produccion no existe para la Gramatica.\nO bien el terminal involucrado no existe en la lista de terminales.")
                    else:                                
                                #print("recursivo por la derecha")
                        for c in range(len(self.boveda[i].getTerminales())):
                            if NT2[1] == self.boveda[i].getTerminales()[c]:
                                flag3+=1
                                        #input("terminal")

                        for a in range(len(self.boveda[i].getNoTerms())):
                            if NT1[0]== self.boveda[i].getNoTerms()[a].getName():
                                flag1+=1
                                inicial = self.boveda[i].getNoTerms()[a]

                                if self.boveda[i].getNoTerms()[a].getSalidas():                                    
                                    for k in range(len(self.boveda[i].getNoTerms()[a].getSalidas())):
                                        if NT2[1] ==self.boveda[i].getNoTerms()[a].getSalidas()[k]:
                                            banderita+=1                                        
                                    if banderita == 0:
                                        self.boveda[i].getNoTerms()[a].getSalidas().append(NT2[1])
                                else:
                                    self.boveda[i].getNoTerms()[a].getSalidas().append(NT2[1])
                                        #input("inicio")

                        for b in range(len(self.boveda[i].getNoTerms())):
                            if NT2[2]== self.boveda[i].getNoTerms()[b].getName():
                                flag2+=1
                                final = self.boveda[i].getNoTerms()[b]
                                        #input("final")                                

                        if flag1!=0 and flag2!=0 and flag3!=0:
                            if banderita==0:                        
                                proud = Produccion(inicial, final, NT2[1])
                                self.boveda[i].getProducciones().append(proud)
                            else:
                                print("Ésta acción no se completó.\nUsted está ingresando una producción que ya existe.")
                        else:
                            print("Almenos un No terminal que está involucrado en ésta produccion no existe para la Gramatica.\nO bien el terminal involucrado no existe en la lista de terminales.")                            
                elif len(NT2)==2:
   #                         print("viene epsilon o terminal")
                    if NT2[1]=="$":
    #                            print("terminal de aceptacion")
                        badera = 0
                        for a in range(len(self.boveda[i].getNoTerms())):
                            if NT1[0] == self.boveda[i].getNoTerms()[a].getName():                                        
                                badera+=1
                            
                                self.boveda[i].getNoTerms()[a].setEpsilon(True)
                            
                                
                        ##modiificación
                        #print("vamo a buscar el terminal")
                        for c in range(len(self.boveda[i].getTerminales())):
                            if NT2[1] == self.boveda[i].getTerminales()[c]:
                                flag3+=1
                                        #input("terminal")

                        for a in range(len(self.boveda[i].getNoTerms())):
                            if NT1[0]== self.boveda[i].getNoTerms()[a].getName():                                        
                                flag2+=1
                                inicial = self.boveda[i].getNoTerms()[a].getName()
                                if self.boveda[i].getNoTerms()[a].getSalidas():                                    
                                    for k in range(len(self.boveda[i].getNoTerms()[a].getSalidas())):
                                        if NT2[1] ==self.boveda[i].getNoTerms()[a].getSalidas()[k]:
                                            banderita+=1                                        
                                    if banderita == 0:
                                        self.boveda[i].getNoTerms()[a].getSalidas().append(NT2[1])
                                else:
                                    self.boveda[i].getNoTerms()[a].getSalidas().append(NT2[1])
                                        #input("inicio")

                        if flag2 != 0 and flag3 != 0:
                            if banderita==0:
                                nova = noTerminal(" ")
                                proud = Produccion(inicial, nova.getName(), NT2[1])
                                self.boveda[i].getProducciones().append(proud)
                            else:
                                print("Ésta acción no se completó.\nUsted está ingresando una producción que ya existe.")
                        else:
                            print("El No Terminal y/o el Terminal involucrado en ésta producción no existe para la gramatica.")
                        #fin modificaciión
                                        
                    else:
                        #print("vamo a buscar el terminal")
                        for c in range(len(self.boveda[i].getTerminales())):
                            if NT2[1] == self.boveda[i].getTerminales()[c]:
                                flag3+=1
                                        #input("terminal")

                        for a in range(len(self.boveda[i].getNoTerms())):
                            if NT1[0]== self.boveda[i].getNoTerms()[a].getName():                                        
                                flag2+=1
                                inicial = self.boveda[i].getNoTerms()[a]
                                if self.boveda[i].getEstados()[a].getSalidas():                                    
                                    for k in range(len(self.boveda[i].getNoTerms()[a].getSalidas())):
                                        if NT2[1] ==self.boveda[i].getNoTerms()[a].getSalidas()[k]:
                                            banderita+=1                                        
                                    if banderita == 0:
                                        self.boveda[i].getNoTerms()[a].getSalidas().append(NT2[1])
                                else:
                                    self.boveda[i].getNoTerms()[a].getSalidas().append(NT2[1])
                                        #input("inicio")

                        if flag2 != 0 and flag3 != 0:
                            if banderita==0:
                                proud = Produccion(inicial, self.boveda[i].getPrede(), NT2[1])
                                self.boveda[i].getProducciones().append(proud)
                            else:
                                print("Ésta acción no se completó.\nUsted está ingresando una producción que ya existe.")
                        else:
                            print("El No Terminal y/o el Terminal involucrado en ésta producción no existe para la gramatica.")

##cargar archivos
##menu
    def cargaAFD(self):
        nombre = input("Ingrese el nombre del archivo para generar el AFD: ")
        archivoAFDS = open(nombre,'r') 
        Datos = archivoAFDS.read()
        archivoAFDS.close()
        divisonAFDS = Datos.split('%')
        try:
            divisonAFDS.remove('')
        except:
            pass
        listaAutomatas = []
        #ciclo for para extraer los datos de cada automata, 
        # ponerlos en una lista de listas y eliminar elementos en blanco
        for i in range(len(divisonAFDS)):
            automata = divisonAFDS[i].split('\n')
            try:
                automata.remove('')
                automata.remove('')
            except:
                pass
            listaAutomatas.append(automata)
        #Ciclo for para empezar a crear objetos Aefede
        for a in range(len(listaAutomatas)):
            #verificando si el automata que se quiere agregar ya existe
            flag = 0
            for a in range(len(self.boveda)):
                if listaAutomatas[i][0] == self.boveda[a].getName():
                    flag +=1
            if flag == 0: #el automata no existe y lo agregamos
                #tratamos con el nombre
                name = str(listaAutomatas[i][0])
                aefede = Aefede(name)
                self.boveda.append(aefede)
                #tratamos con los estados
                estrato = listaAutomatas[i][1].split(',')
                for j in range(len(estrato)):
                    self.CrearEstados(name,str(estrato[j]))
                #tratamos con el alfabeto
                alpha = listaAutomatas[i][2].split(',')
                for k in range(len(alpha)):
                    self.CrearAlfabeto(name,str(alpha[k]))
                #tratamos con el estado inicial
                self.AsignarEstadoInicial(name,str(listaAutomatas[i][3]))
                #tratamos con los estados de aceptacion
                try:
                    aceptaciones = listaAutomatas[i][4].split(',')
                    aceptaciones.remove('')
                except:
                    pass
                for l in range(len(aceptaciones)):
                    self.Acetona(name,str(aceptaciones[l]))
                #Tratamos con las transiciones
                for m in range(len(listaAutomatas[i])):
                    if m >=5:
                        self.Transiciones(name,str(listaAutomatas[i][m]))
                input("AFD cargado correctamente.\nPresione ENTER para volver al menú principal.")

            else:
                input("El AFD que se quiere agregar ya existe en memoria")
    
    def cargarGR(self):
        print()
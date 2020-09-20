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
                self.clrsrc()
                self.escribirAFD()
                self.clrsrc()
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
                    self.IngresarTerminales(name)
                    self.NoTerminalInicial(name)
                    self.Produu(name)
                self.clrsrc()

            elif opcion == 2:
                self.clrsrc()
                self.cargarGR()
                self.clrsrc()
            elif opcion == 3:
                input("Evaluar cadena")                            
            elif opcion == 4:
                self.clrsrc()
                self.escribirGR()
                self.clrsrc()
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

    def escribirAFD(self):
        print("Lista de automatas finitos deterministas en el sistema:\n")
        for a in range(len(self.boveda)):
            if self.boveda[a].getTipo()=="AFD":
                print("-> "+self.boveda[a].getName())
        nombre = str(input("\nIngrese el nombre del AFD que quiere guardar: "))
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')        
        archivo = open(path_desktop+"\\"+nombre+".afd", 'w')
        estados=""
        alfabeto=""
        estadoInicial=""
        estadosAceptacion=""
        #for para recorrer lista general        
        for i in range(len(self.boveda)):
            if self.boveda[i].getName()==nombre and self.boveda[i].getTipo()=="AFD":
                #agregando nombre
                archivo.writelines(self.boveda[i].getName()+"\n")
                #agregando estados
                for n in range(len(self.boveda[i].getEstados())):
                    if n>=1:
                        estados+=","+self.boveda[i].getEstados[n].getNameE()
                    else:
                        estados=self.boveda[i].getEstados[n].getNameE()
                archivo.writelines(estados+"\n")
                #agregando alfabeto
                for m in range(len(self.boveda[i].getAlfabeto())):
                    if m>=1:
                        alfabeto+=","+self.boveda[i].getAlfabeto()[m]
                    else:
                        alfabeto=self.boveda[i].getAlfabeto()[m]
                archivo.writelines(alfabeto+"\n")
                #agregando estado inicial.
                for o in range(len(self.boveda[i].getEstados())):
                    if self.boveda[i].getEstados()[o].getInicio()==True:
                        estadoInicial=self.boveda[i].getEstados()[o].getNameE()
                archivo.writelines(estadoInicial+"\n")
                #agregando estados de aceptación
                for p in range(len(self.boveda[i].getEstados())):
                    if self.boveda[i].getEstados()[p].getAcepta()==True:
                        if p>=1:
                            estadosAceptacion += ","+self.boveda[i].getEstados()[p].getNameE()
                        else:
                            estadosAceptacion = self.boveda[i].getEstados()[p].getNameE()
                archivo.writelines(estadosAceptacion+"\n")
                #agregando transiciones                
                for q in range(len(self.boveda[i].getTransiciones())):                    
                    archivo.writelines(self.boveda[i].getTransiciones()[q].geteInicial().getNameE()+","+self.boveda[i].getTransiciones()[q].getEntrada()+";"+self.boveda[i].getTransiciones()[q].geteFinal().getNameE()+"\n")                    
                archivo.writelines("%")
        archivo.close()

    def escribirGR(self):
        print("Lista de gramaticas regulares en el sistema:\n")
        for a in range(len(self.boveda)):
            if self.boveda[a].getTipo()=="Gramatica":
                print("-> "+self.boveda[a].getName())
        nombre = str(input("\nIngrese el nombre de la gramatica que quiere guardar: "))
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')        
        archivo = open(path_desktop+"\\"+nombre+".gre", 'w')
        NoTerms=""
        Termis=""
        NTInicial=""
        estadosAceptacion=""
        #for para recorrer lista general        
        for i in range(len(self.boveda)):
            if self.boveda[i].getName()==nombre and self.boveda[i].getTipo()=="Gramatica":
                #agregando nombre
                archivo.writelines(self.boveda[i].getName()+"\n")
                #agregando no terminales
                for n in range(len(self.boveda[i].getNoTerms())):
                    if n>=1:
                        NoTerms+=","+self.boveda[i].getNoTerms[n].getName()
                    else:
                        NoTerms=self.boveda[i].getEstados[n].getNameE()
                archivo.writelines(NoTerms+"\n")
                #agregando terminales
                for m in range(len(self.boveda[i].getTerminales())):
                    if m>=1:
                        Termis+=","+self.boveda[i].getTerminales()[m]
                    else:
                        Termis=self.boveda[i].getTerminales()[m]
                archivo.writelines(Termis+"\n")
                #agregando no terminal inicial.
                for o in range(len(self.boveda[i].getNoTerms())):
                    if self.boveda[i].getNoTerms()[o].getInicio()==True:
                        NTInicial=self.boveda[i].getNoTerms()[o].getName()
                archivo.writelines(NTInicial+"\n")                
                #agregando producciones             
                for q in range(len(self.boveda[i].getProducciones())):                    
                    archivo.writelines(self.boveda[i].getgetProducciones()[q].gettInicial().getName()+">"+self.boveda[i].getProducciones()[q].getTerminal()+" "+self.boveda[i].getProducciones()[q].gettFinal().getName()+"\n")
                for p in range(len(self.boveda[i].getNoTerms())):
                    if self.boveda[i].getNoTerms()[p].getEpsilon()==True:
                        archivo.writelines(self.boveda[i].getNoTerms()[p].getName()+">$")
                archivo.writelines("%")
        archivo.close()
    #wwwwwwwwwwwwwwwwwwwwwwww
    #eeeeeeeeeeeeeeeeeeeeeeee
    ####alllllltoooooo fin menu guardar                          
    
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
                                if estados[1]==self.boveda[i].getEstados()[a].getSalidas()[k]:
                                    banderita+=1                                        
                            if banderita == 0:
                                self.boveda[i].getEstados()[a].getSalidas().append(estados[1])
                        else:
                            self.boveda[i].getEstados()[a].getSalidas().append(estados[1])
                                #input("inicio")
                #validando estado final
                for b in range(len(self.boveda[i].getEstados())):
                    if frag[1]== self.boveda[i].getEstados()[b].getNameE():
                        flag2+=1
                        final = self.boveda[i].getEstados()[b]
                                #input("final")

                if flag1!=0 and flag2!=0 and flag3!=0:
                    if banderita==0:                            
                        trancy = Transicion(inicial, final, estados[1])
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
                            self.boveda[i].getNoTerms()[b].setInicio(True)                                                        
                else:
                    input("El AFD al que intenta asignar un estado inicial no cuenta con ningun estado todavia.")
    
    #Ingreso de producciones
    #vamo a ver
    def Produu(self, nome):
        self.clrsrc()
        print("Gramatica llamada: "+nome+"\nIngresando Producciones. Escriba >>salir<< para detenerse.")
        print("Ejemplo de la sintaxis de ingreso: \"A>a B\"")
        salida = True
        while salida:        
            trans = input("\nIngrese una producción: ")
            if trans != "salir":
                self.CrearProducciones(nome,trans)
            else:
                salida = False
    
    def CrearProducciones(self,nome,produc):
        frag = produc.split('>')
                #  0  , 1
        #Frag = ["A","0 B"]
        #estados = ["0","B"]
        frag2 = frag[1].split(' ')
        if len(frag2)==2:
            for i in range(len(self.boveda)):
                if nome == self.boveda[i].getName() and self.boveda[i].getTipo()=="Gramatica":
                    flag1=0
                    flag2=0
                    flag3=0
                    banderita=0
                    inicial = None
                    final = None
                    #Validando terminal involucrado en la producción.
                    for c in range(len(self.boveda[i].getTerminales())):
                        if frag2[0] == self.boveda[i].getTerminales()[c]:
                            flag3+=1
                                    #input("terminal")

                    #validando estado inicial y que no haya mas de una transición con la misma terminal
                    for a in range(len(self.boveda[i].getNoTerms())):
                        if frag[0] == self.boveda[i].getNoTerms()[a].getName():
                            flag1+=1
                            inicial = self.boveda[i].getNoTerms()[a]
                            if self.boveda[i].getNoTerms()[a].getSalidas():

                                for k in range(len(self.boveda[i].getNoTerms()[a].getSalidas())):
                                    if frag2[0]==self.boveda[i].getNoTerms()[a].getSalidas()[k]:
                                        banderita+=1                                        
                                if banderita == 0:
                                    self.boveda[i].getNoTerms()[a].getSalidas().append(frag2[0])
                            else:
                                self.boveda[i].getNoTerms()[a].getSalidas().append(frag2[0])
                                    #input("inicio")
                    #validando estado final
                    for b in range(len(self.boveda[i].getNoTerms())):
                        if frag2[1]== self.boveda[i].getNoTerms()[b].getName():
                            flag2+=1
                            final = self.boveda[i].getEstados()[b]
                                    #input("final")

                    if flag1!=0 and flag2!=0 and flag3!=0:
                        if banderita==0:                            
                            trancy = Transicion(inicial, final, frag2[0])
                            self.boveda[i].getTransiciones().append(trancy)
                        else:
                            print("Ésta acción no se completó.\nUsted está tratando de crear ambiguedad.")
                    else:
                        print("Almenos un No terminal que está involucrado en ésta producción no existe en la lista de No terminales de esta gramatica.\nO bien el terminal involucrado no existe en el alfabeto de la gramatica")
        else:#aceptación de cadena
            if frag[1]=='$':
                for n in range(len(self.boveda)):
                    if nome == self.boveda[n].getName() and self.boveda[n].getTipo()=="Gramatica":
                        for m in range(len(self.boveda[n].getNoTerms())):
                            if frag[0]==self.boveda[n].getNoTerms()[m].getName():
                                self.boveda[n].getNoTerms()[m].setEpsilon(True)                        
        
##cargar archivos
##menu
    def cargaAFD(self):
        nombre = input("Ingrese el nombre del archivo para generar el/los AFD/s: ")
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
        nombre = input("Ingrese el nombre del archivo para generar la/s gramatica/s: ")
        archivoGRS = open(nombre,'r') 
        Datos = archivoGRS.read()
        archivoGRS.close()
        divisonGRS = Datos.split('%')
        try:
            divisonGRS.remove('')
        except:
            pass
        listaGramaticas = []
        #ciclo for para extraer los datos de cada Gramatica, 
        # ponerlos en una lista de listas y eliminar elementos en blanco
        for i in range(len(divisonGRS)):
            automata = divisonGRS[i].split('\n')
            try:
                automata.remove('')
                automata.remove('')
            except:
                pass
            listaGramaticas.append(automata)
        #Ciclo for para empezar a crear objetos NoTerminales
        for a in range(len(listaGramaticas)):
            #verificando si la gramatica que se quiere agregar ya existe
            flag = 0
            for a in range(len(self.boveda)):
                if listaGramaticas[i][0] == self.boveda[a].getName():
                    flag +=1
            if flag == 0: #el automata no existe y lo agregamos
                #tratamos con el nombre
                name = str(listaGramaticas[i][0])
                gramatica = noTerminal(name)
                self.boveda.append(gramatica)
                #tratamos con los no terminales
                noTerms = listaGramaticas[i][1].split(',')
                for j in range(len(noTerms)):
                    self.CrearNoTerminal(name,str(noTerms[j]))
                #tratamos con los terminales
                zonas4 = listaGramaticas[i][2].split(',')
                for k in range(len(zonas4)):
                    self.CrearTerminales(name,str(zonas4[k]))
                #tratamos con el no terminal inicial
                self.AsignarNoTerminalInicial(name,str(listaGramaticas[i][3]))                
                #Tratamos con las producciones
                for m in range(len(listaGramaticas[i])):
                    if m >=4:
                        self.CrearProducciones(name,str(listaGramaticas[i][m]))
                input("Gramatica cargada correctamente.\nPresione ENTER para volver al menú principal.")

            else:
                input("La gramatica que se quiere agregar ya existe en memoria")
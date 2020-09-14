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
        valor ="teniaquehacerloYela"
        teniaque = Aefede(valor)
        self.boveda.append(teniaque)        
        #self.GRS = []

    def Iniciar(self):
        self.clrsrc()
        print("Lenguajes Formales de programación")
        print("Sección B-")
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
            print("1- Crear/Modificar AFD")
            print("2- Crear/Modificar Gramática")
            print("3- Evaluar Cadenas")
            print("4- Cargar Archivo de Entrada")
            print("5- Guardar archivo .afd o .grm")
            print("6- Reportes")
            print("7- Salir\n")
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                self.clrsrc()
                try:    
                    self.SubAFD()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion == 2:
                self.clrsrc()
                try:
                    self.SubGR()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion == 3:
                self.clrsrc()
                try:
                    self.SubEChain()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion == 4:
                self.clrsrc()
                try:
                    self.SubUpFi()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion == 5:
                self.clrsrc()
                try:
                    self.Save()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion == 6:
                self.clrsrc()
                try:
                    self.Reporte()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion == 7:
                self.clrsrc()        
                #self.probando()                
                exit()                               
            else:
                self.clrsrc()
                input("Ingrese una opción valida")

##Menu de segundo grado

###pinche menu de aefedes
    def SubAFD(self):
        self.clrsrc()
        rashos = input('Ingrese el nombre del AFD: ')
        name = str(rashos)
        flag=0
        for i in range(len(self.boveda)):
            if name == self.boveda[i].getName() and self.boveda[i].getTipo()=="AFD":
                flag +=1
        if flag!=0:
            decision = input("\nEl elemento ya existe, ¿desea modificarlo?: si/no\n")
            if decision == "si":
                salidas = True
                while salidas:
                    self.clrsrc()
                    print("********** Menú de AFD **********\n")
                    print('1- Ingresar estados')
                    print('2- Ingresar alfabeto')
                    print('3- Estado inicial')
                    print('4- Estados de aceptaciòn')
                    print('5- Transiciones')
                    print('6- Ayuda')
                    print('7- Menu principal\n')
                    opcion = int(input('Ingrese una opción: '))
                    if opcion == 1:
                            #input("ingresando estados")
                        self.clrsrc()
                        try:
                            self.IngresarEstados(name)
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                            #self.probando()
                    elif opcion == 2:
                        self.clrsrc()
                        try:
                            self.IngresarAlfabeto(name)
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 3:
                        self.clrsrc()
                        try:
                            self.EstadoInicial(name)
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                            #self.probando()
                    elif opcion == 4:
                        self.clrsrc()
                        try:
                            self.Aceptation(name)
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                            #self.probando()
                    elif opcion == 5:
                        self.clrsrc()
                        try:
                            self.Transicion(name)
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 6:
                        self.clrsrc()
                        self.Help()
                    elif opcion == 7:
                        salidas = False
                        try:
                            self.Menu()
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    else:
                        self.clrsrc()
                        input("Ingrese una opción valida")
            elif decision == "no":
                try:
                    self.Menu()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
        else:
            nuevoAFD = Aefede(name)
            predetermindado = Estado("PR")
            predetermindado.setAcepta(True)
            nuevoAFD.setPrede(predetermindado)
            self.boveda.append(nuevoAFD)             
            salidas = True
            while salidas:
                self.clrsrc()
                print("********** Menú de AFD **********\n")
                print('1- Ingresar estados')
                print('2- Ingresar alfabeto')
                print('3- Estado inicial')
                print('4- Estados de aceptaciòn')
                print('5- Transiciones')
                print('6- Ayuda')
                print('7- Menu principal\n')
                opcion = int(input('Ingrese una opción: '))
                if opcion == 1:
                        #input("ingresando estados")
                    self.clrsrc()
                    try:
                        self.IngresarEstados(name)
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                        #self.probando()
                elif opcion == 2:
                    self.clrsrc()
                    try:
                        self.IngresarAlfabeto(name)
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                elif opcion == 3:
                    self.clrsrc()
                    try:
                        self.EstadoInicial(name)
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                        #self.probando()
                elif opcion == 4:
                    self.clrsrc()
                    try:
                        self.Aceptation(name)
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                        #self.probando()
                elif opcion == 5:
                    self.clrsrc()
                    try:
                        self.Transicion(name)                       
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                elif opcion == 6:
                    self.clrsrc()
                    self.Help()
                elif opcion == 7:
                    salidas = False
                    try:
                        self.Menu()
                    except:
                        print("Parece que tenemos problemas, se va a estabilizar.")
                else:
                    self.clrsrc()
                    input("Ingrese una opción valida")

    #pinche menu de gramaticas
    def SubGR(self):
        self.clrsrc()
        name = str(input('Ingrese el nombre de la gramatica: '))
        flag = 0
        for i in range(len(self.boveda)):
            if name == self.boveda[i].getName() and self.boveda[i].getTipo()=="Gramatica":
                flag+=1
        if flag!=0:
            desicion = input("\nEl elemento ya existe, ¿desea modificarlo?: si/no\n")
            if desicion == "si":
                salidas = True
                while salidas:
                    self.clrsrc()
                    print("********** Menú de Gramaticas **********\n")
                    print('1- Ingresar no terminales')
                    print('2- Ingresar terminales')
                    print('3- No terminal inicial')
                    print('4- Producciones')
                    print('5- Gramática trasformada')
                    print('6- Ayuda')
                    print('7- Menu principal\n')
                    opcion = int(input('Ingrese una opción: '))
                    if opcion == 1:
                        self.clrsrc()
                        try:
                            self.IngresarNT(name)                        
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 2:
                        self.clrsrc()
                        try:
                            self.IngresarTerminales(name)                        
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 3:
                        self.clrsrc()
                        try:
                            self.NoTerminalInicial(name)
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 4:
                        self.clrsrc()
                        try:
                            self.Produu(name)
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    elif opcion == 5:
                        input("gramatica transformada")
                    elif opcion == 6:
                        self.clrsrc()
                        self.Help()
                    elif opcion == 7:
                        salidas = False
                        try:
                            self.Menu()
                        except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                    else:
                        self.clrsrc()
                        input("Ingrese una opción valida")
            elif desicion == "no":
                    #input("Ingrese un nuevo nombre.")
                try:
                    self.Menu()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
        else:
            nuevaGR= Gramatica(name)
            nuevaGR.getTerminales().append("epsilon")
            predetermindado = noTerminal("PR")
            predetermindado.setEpsilon(True)
            nuevaGR.setPrede(predetermindado)
            self.boveda.append(nuevaGR)
            salidas = True
            while salidas:
                self.clrsrc()
                print("********** Menú de Gramáticas **********\n")
                print('1- Ingresar no Terminales')
                print('2- Ingresar Terminales')
                print('3- No terminal inicial')
                print('4- Producciones')
                print('5- Grámatica transformada')
                print('6- Ayuda')
                print('7- Menu principal\n')
                opcion = int(input('Ingrese una opción: '))
                if opcion == 1:
                    self.clrsrc()
                    try:
                        self.IngresarNT(name)
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                elif opcion == 2:
                    self.clrsrc()
                    try:
                        self.IngresarTerminales(name)
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                elif opcion == 3:
                    self.clrsrc()
                    try:
                        self.NoTerminalInicial(name)
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                elif opcion == 4:
                    self.clrsrc()
                    try:
                        self.Produu(name)
                    except:
                            print("Parece que tenemos problemas, se va a estabilizar.")
                elif opcion == 5:
                    input("Gramatica transformada")
                elif opcion == 6:
                    self.clrsrc()
                    self.Help()
                elif opcion == 7:
                    salidas = False
                    try:
                        self.Menu()
                    except:
                        print("Parece que tenemos problemas, se va a estabilizar.")
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
    def SubUpFi(self):
        salida = True
        while salida:
            self.clrsrc()
            print("********** Menú Carga de Archivos **********\n")
            print('1- Automata Finito Determinista')
            print('2- Grámatica Regular')
            print('3- Menú Principal\n')
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                self.clrsrc()
                try:
                    self.cargaAFD()            
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion ==2:
                self.clrsrc()
                try:
                    self.cargarGR()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion == 3:
                salida = False
                try:
                    self.Menu()
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            else:
                self.clrsrc()
                input("Ingrese una opción valida")

    #pinche menu guardar
    def Save(self):
        indice = input("Ingrese el nombre del AFD o la Gramatica a guardar: ")
        flagAFD = 0
        flagGR = 0
        for a in range(len(self.boveda)):
            if indice == self.boveda[a].getName() and self.boveda[a].getTipo()=="AFD":
               flagAFD+=1
            if indice == self.boveda[a].getName() and self.boveda[a].getTipo()=="Gramatica": 
                flagGR+=1
            #ninguno existe
        if flagAFD==0 and flagGR == 0:
            input("\nParece que el elemento que busca guardar no existe en memoria, Intentelo otra vez.")
            #gramatica no existe 
            #afd existe
        elif flagAFD!=0 and flagGR == 0:
            print("\nHemos comprobado que el elemento solo existe como AFD. Pero se puede generar la gramatica si es lo que quiere.\n")
            tipo = input("Ingrese \"AFD\" para guardar el automata o \"GR\" para la gramatica: ")
            name = input("Por ultimo ingrese el nombre con el que desea guardar el archivo : ")
            if tipo=="AFD":
                try:
                    self.escribirAFD(name,indice)
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif tipo=="GR":
                try:
                    self.generarGR(indice)
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
                try:
                    self.escribirGR(name,indice)
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            #gramatica existe
            #afd no existe
        elif flagAFD==0 and flagGR!=0:
            print("\nHemos comprobado que el elemento solo existe como Gramatica. Pero se puede generar el AFD si es lo que quiere.\n")
            tipo = input("Ingrese \"AFD\" para guardar el automata o \"GR\" para la gramatica: ")
            name = input("Por ultimo ingrese el nombre con el que desea guardar el archivo : ")
            if tipo=="AFD":
                try:
                    self.generarAFD(indice)
                    self.escribirAFD(name,indice)
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif tipo=="GR":
                try:
                    self.escribirGR(name,indice)
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
        elif flagAFD!=0 and flagGR!=0:
            print("\nHemos comprobado que el elemento existe como Gramatica y como AFD.\n")
            tipo = input("Ingrese \"AFD\" para guardar el automata o \"GR\" para la gramatica: ")
            name = input("Por ultimo ingrese el nombre con el que desea guardar el archivo : ")
            if tipo == "AFD":
                try:
                    self.escribirAFD(name,indice)
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")
            elif tipo == "GR":
                try:
                    self.escribirGR(name,indice)
                except:
                    print("Parece que tenemos problemas, se va a estabilizar.")

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
        archivo = open("C:\\Users\\almxo\\Desktop\\"+nombre+".afd", 'w')
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
        archivo = open("C:\\Users\\almxo\\Desktop\\"+nombre+".grm", 'w')
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
    
# funciones chidas
    def probando(self):
        for i in range(len(self.boveda)):
            if self.boveda[i].getTipo() == "Gramatica":
                print(self.boveda[i].getName())
                for a in range(len(self.boveda[i].getProducciones())):
                    print(self.boveda[i].getProducciones()[a].gettInicial()+" > "+self.boveda[i].getProducciones()[a].getTerminal()+" "+self.boveda[i].getProducciones()[a].gettFinal())
                print("fin")

        for a in range(len(self.boveda)):
            if self.boveda[a].getTipo() == "AFD":
                print(self.boveda[a].getName())
                print("estados:")
                for p in range(len(self.boveda[a].getEstados())):
                    print(self.boveda[a].getEstados()[p].getNameE()+"| Aceptación: "+self.boveda[a].getEstados()[p].getAcepta())
                print("ALFABETO")
                for p in range(len(self.boveda[a].getAlfabeto())):
                    print(self.boveda[a].getAlfabeto()[p])
                for q in range(len(self.boveda[a].getTransiciones())):
                    print(self.boveda[a].getTransiciones()[q].geteInicial()+","+self.boveda[a].getTransiciones()[q].geteFinal()+";"+self.boveda[a].getTransiciones()[q].getEntrada())
        #print("afd: " + self.boveda[1].getName())
        #print("trancy inicial: "+ self.boveda[1].getTransiciones()[0].geteInicial().getNameE())
        #print("trancy final: "+ self.boveda[1].getTransiciones()[0].geteFinal().getNameE())
        #print("trancy terminal: "+ self.boveda[1].getTransiciones()[0].getEntrada())
        #print("estado 1: "+ self.boveda[1].getEstados()[0].getNameE()+" Aceptación: "+self.boveda[1].getEstados()[0].getAcepta())
        #print("estado 2: "+ self.boveda[1].getEstados()[1].getNameE()+" Aceptación: "+self.boveda[1].getEstados()[1].getAcepta())
        #print("estado 3: "+ self.boveda[1].getEstados()[2].getNameE()+" Aceptación: "+self.boveda[1].getEstados()[2].getAcepta())
        #print("estado 4: "+ self.boveda[1].getEstados()[3].getNameE()+" Aceptación: "+self.boveda[1].getEstados()[3].getAcepta())

        #print("\nafd: " + self.boveda[1].getName())
        #print("elemento 1: "+ self.boveda[1].getAlfabeto()[0])
        #print("elemento 2: "+ self.boveda[1].getAlfabeto()[1])
        #print("elemento 3: "+ self.boveda[1].getAlfabeto()[2])
        #print("elemento 4: "+ self.boveda[1].getAlfabeto()[3])
        #for i in range(len(self.boveda[1].getEstados())):
            #print(self.boveda[1].getEstados()[i].getNameE())
            #print(estesi[1].getEstados()[i].getNameE())
        input("perate")        
            
    def clrsrc(self):
        os.system("cls")

    def Help(self):
        print("Lenguajes Formales de Programación \nAuxiliar: Luis Yela \n-> 9 <-")
        input("Pulsa enter para continuar: ")
    
    #santo vergueo para un pinche estado
    def IngresarEstados(self, nome):
        print("AFD llamado: "+nome+"\nEscriba >>salir<< para dejar de ingresar estados")
        salida = True
        while salida:   
            dato = str(input("\nIngrese un estado para el AFD: "))
            estado = dato.upper()
            if dato != "salir":                
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
                    state.setInicio(True)
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
                if self.boveda[a].getAlfabeto():    
                    flag = 0                                                                                
                    for i in range(len(self.boveda[a].getAlfabeto())):
                        if alfa == self.boveda[a].getAlfabeto()[i]:                                    
                            flag+=1

                    if flag == 0:
                        self.boveda[a].getAlfabeto().append(alfa)
                    else:
                        print("El elemento ya existe en el alfabeto.")
                else:
                    self.boveda[a].getAlfabeto().append(alfa)
    #vergueo del estado inicial
    def EstadoInicial(self, nome):
        print("AFD llamado: "+nome+"\n")
        dato = str(input("Ingrese un estado existente para declararlo como estado inicial del AFD: "))
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
    def Transicion(self, nome):
        
        salida = True
        while salida:
            self.clrsrc()
            print("AFD llamado: "+nome+"\nEliga el modo de ingreso de las transiciones.")
            print("1- Modo 1")
            print("2- Modo 2")
            print("3- Volver al menu de AFDs\n")
            opcion = int(input("Ingrese una opcion: "))
            if opcion==1:
                self.clrsrc()
                #try:
                self.Modo1(nome)
                #except:
                    #print("Parece que tenemos problemas, se va a estabilizar.")
            elif opcion == 2:
                self.clrsrc()
                self.Modo2(nome)
            elif opcion == 3:
                salida = False
                self.Menu()
            else:
                self.clrsrc()
                print("Ingrese una opción valida")
    
    #modos de ingreso de las transiciones
    def Modo1(self, nome):
        self.clrsrc()
        print("AFD llamado: "+nome+"\nIngresando transiciones. Escriba >>salir<< para detenerse.")
        print("Ejemplo de la sintaxis de ingreso: \"A,B;0\"")
        salida = True
        while salida:        
            trans = input("\nIngrese una transición: ")
            if trans != "salir":
                #try:
                self.TransicionesModo1(nome,trans)                
                #except:
                    #print("Parece que tenemos problemas, se va a estabilizar.")
            else:
                salida = False

    def TransicionesModo1(self, nome, trans):
        frag = trans.split(';')
        estados = frag[0].split(',')
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()=="AFD":
                flag1=0
                flag2=0
                flag3=0
                banderita=0
                inicial = None
                final = None
                for c in range(len(self.boveda[i].getAlfabeto())):
                    if frag[1] == self.boveda[i].getAlfabeto()[c]:
                        flag3+=1
                                #input("terminal")

                for a in range(len(self.boveda[i].getEstados())):
                    if estados[0] == self.boveda[i].getEstados()[a].getNameE():
                        flag1+=1
                        inicial = self.boveda[i].getEstados()[a].getNameE()
                        if self.boveda[i].getEstados()[a].getSalidas():
                                    
                            for k in range(len(self.boveda[i].getEstados()[a].getSalidas())):
                                if frag[1]==self.boveda[i].getEstados()[a].getSalidas()[k]:
                                    banderita+=1                                        
                            if banderita == 0:
                                self.boveda[i].getEstados()[a].getSalidas().append(frag[1])
                        else:
                            self.boveda[i].getEstados()[a].getSalidas().append(frag[1])
                                #input("inicio")

                for b in range(len(self.boveda[i].getEstados())):
                    if estados[1]== self.boveda[i].getEstados()[b].getNameE():
                        flag2+=1
                        final = self.boveda[i].getEstados()[b].getNameE()
                                #input("final")                       

                if flag1!=0 and flag2!=0 and flag3!=0:
                    if banderita==0:                            
                        trancy = Transicion(inicial, final, frag[1])
                        self.boveda[i].getTransiciones().append(trancy)
                    else:
                        print("Ésta acción no se completó.\nUsted está tratando de crear un Automata Finito NO Determinista o Está ingresando una transición que ya existe.")
                else:
                    print("Almenos un estado que está involucrado en ésta transición no existe en la lista de estados de este AFD.\nO bien el terminal involucrado no existe en el alfabeto del AFD")

    def Modo2(self, nome):
        self.clrsrc()
        print("AFD llamado: "+nome+"\n")
        entrada1 =str(input("Ingrese el alfabeto separados por comas: "))
        entrada2 = str(input("Ingrese los estados iniciales separados por comas: "))
        print("\nEjemplo de sintaxis: A,C;A,C;B,D")
        entrada3 = str(input("Ingrese los estados finales:"))
        alfabeto= entrada1.split(',')
        eIni= entrada2.split(',')
        eFini = entrada3.split(';')
        entraModo1=[]
        if eIni.__len__()==eFini.__len__():
            for a in range(len(eIni)):
                vamo = eFini[a].split(',')
                if vamo[0]!="-":
                    transmetro = eIni[a]+","+vamo[0]+";"+alfabeto[0] 
                    entraModo1.append(transmetro)

            for b in range(len(eIni)):
                vamo = eFini[b].split(',')
                if vamo[1]!="-":
                    transmetro = eIni[b]+","+vamo[1]+";"+alfabeto[1] 
                    entraModo1.append(transmetro)

        for i in range(len(entraModo1)):
            trans = str(entraModo1[i])
            self.TransicionesModo1(nome, trans)

##gramaticas
##Gramaticas
##Gramaticas
#copia del santo vergueo para un pinche estado y modificado para un no terminal
    def IngresarNT(self, nome):
        print("Gramática llamada: "+nome+"\nEscriba >>salir<< para dejar de ingresar No Terminales")
        salida = True
        while salida:   
            dato = str(input("\nIngrese un No terminal para la Gramática: "))
            NT = dato.upper()
            if dato != "salir":                
                self.CrearNoTerminal(nome,NT)
            else:
                salida = False

    def CrearNoTerminal(self,nome,NT):
        terminator = noTerminal(NT)                
        for a in range(len(self.boveda)):                    
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()== "Gramatica":                        
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
                    terminator.setInicio(True)
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
    
    #Copia del vergueo del estado inicial para gramaticas
    def NoTerminalInicial(self, nome):
        print("Gramatica llamada: "+nome+"\n")
        dato = str(input("Ingrese un No Terminal existente para declararlo como inicial: "))
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
                                inicial = self.boveda[i].getNoTerms()[a].getName()
#                                        input("inicio")

                        for b in range(len(self.boveda[i].getNoTerms())):
                            if NT2[1]== self.boveda[i].getNoTerms()[b].getName():
                                flag2+=1
                                final = self.boveda[i].getNoTerms()[b].getName()
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

                        for b in range(len(self.boveda[i].getNoTerms())):
                            if NT2[2]== self.boveda[i].getNoTerms()[b].getName():
                                flag2+=1
                                final = self.boveda[i].getNoTerms()[b].getName()
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
                    if NT2[1]=="epsilon":
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
##menu, 
    def cargaAFD(self):
        nombre = input("Ingrese el nombre del archivo para generar el AFD: ")
        name = nombre.split('.')
        flag = 0
        for i in range(len(self.boveda)):
            if name[0] == self.boveda[i].getName():
                flag+=1
        if flag ==0:
            nuevoAFD = Aefede(name[0])
            predetermindado = Estado("PR")
            predetermindado.setAcepta(True)
            nuevoAFD.setPrede(predetermindado)
            self.boveda.append(nuevoAFD)            
            archivo = open(nombre,'r')
            tela = archivo.read()
            archivo.close()
            olvido=tela.split('\n')
            #input("HAGA CASO OMISO A LOS SIGUIENTES MENSAJES, EL AFD SE CREARÁ CON EXITO.")
            for a in range(len(olvido)):
                estados = olvido[a].split(';')
                atributo1=estados[0].split(',')
                atributo2=estados[1].split(',')
                self.CrearEstados(name[0],atributo1[0])
                self.CrearEstados(name[0],atributo1[1])
                self.CrearAlfabeto(name[0],atributo1[2])

                if atributo2[0]=="true":
                    self.Acetona(name[0],atributo1[0])
                elif atributo2[0]=="false":
                    self.AcetonaInverso(name[0],atributo1[0])

                if atributo2[1]=="true":
                    self.Acetona(name[0],atributo1[1])
                elif atributo2[1]=="false":
                    self.AcetonaInverso(name[0],atributo1[1])

            for f in range(len(olvido)):
                estados = olvido[f].split(';')
                atributo1=estados[0].split(',')
                atributo2=estados[1].split(',')
                trans= atributo1[0]+","+atributo1[1]+";"+atributo1[2]                
                self.TransicionesModo1(name[0],trans)
            

            
        else:
            input("El elemento ya existe en memoria, pueda que haya sido cargado previamente.\nO bien ser creado desde el menu de creación.")
    
    def cargarGR(self):
        nombre = input("Ingrese el nombre del archivo para generar la Gramatica: ")
        name = nombre.split('.')
        flag = 0
        for i in range(len(self.boveda)):
            if name[0] == self.boveda[i].getName():
                flag+=1
        if flag ==0:
            nuevoGR = Gramatica(name[0])
            nuevoGR.getTerminales().append("epsilon")
            predetermindado = noTerminal("PR")
            predetermindado.setEpsilon(True)
            nuevoGR.setPrede(predetermindado)
            self.boveda.append(nuevoGR)            
            archivo = open(nombre, 'r')
            tela = archivo.read()
            archivo.close()
            olvido=tela.split('\n')
            #input("HAGA CASO OMISO A LOS SIGUIENTES MENSAJES, EL AFD SE CREARÁ CON EXITO.")
            for a in range(len(olvido)):
                noter = olvido[a].split('>')
                parte1=noter[0].split(' ')
                parte2=noter[1].split(' ')
                self.CrearNoTerminal(name[0],parte1[0])
                if len(parte2)==3:
                    if parte2[1].isupper()==True:
                        nuevoGR.setIzquierda(True)
                        self.CrearNoTerminal(name[0],parte2[1])
                        self.CrearTerminales(name[0],parte2[2])
                    else:
                        self.CrearNoTerminal(name[0],parte2[2])
                        self.CrearTerminales(name[0],parte2[1])

                elif len(parte2)==2:
                    if parte2[1]!="epsilon":
                        self.CrearTerminales(name[0],parte2[1])
            
            for z in range(len(olvido)):
                self.CrearProducciones(name[0],olvido[z])
            
        else:
            input("El elemento ya existe en memoria, pueda que haya sido cargado previamente.\nO bien ser creado desde el menu de creación.")
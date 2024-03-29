import os
from io import open 
import codecs
from Armeria import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import subprocess

class Menu():
    def __init__(self):        
        self.boveda = []
        valor ="  "
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
        self.Menu()             
##menu primer grado
    def Menu(self):
        salida = True		
        while salida:
            try:
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
            except:
                self.Menu()

##Menu de segundo grado
### menu de aefedes
    def SubAFD(self):
        self.clrsrc()
        salida1 = True
        while salida1:
            try:
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
                    for a in range(len(self.boveda)):
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
                    self.clrsrc()
                    self.SubEChainAFD()
                    self.clrsrc()
                elif opcion == 4:
                    self.clrsrc()
                    self.escribirAFD()
                    self.clrsrc()
                elif opcion == 5:
                    self.clrsrc()
                    self.generarHermosoPFD_AFD()
                    self.clrsrc()
                elif opcion == 6:
                    self.clrsrc()
                    self.generarGramaticaConsola()
                    self.clrsrc()
                elif opcion == 7:
                    salida1 = False                
                else:
                    self.clrsrc()
                    input("Ingrese una opción valida")
            except:
                self.SubAFD()

    # menu de gramaticas
    def SubGR(self):
        self.clrsrc()
        salida2 = True
        while salida2:            
            try:
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
                    for a in range(len(self.boveda)):
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
                    self.clrsrc()
                    self.SubEChainGR()
                    self.clrsrc()
                elif opcion == 4:
                    self.clrsrc()
                    self.cargarGR_Izquierda()
                    self.clrsrc()
                elif opcion == 5:
                    self.clrsrc()
                    self.escribirGR()
                    self.clrsrc()
                elif opcion == 6:
                    self.clrsrc()
                    self.generarHermosoPFD_GR()
                    self.clrsrc()
                elif opcion == 7:
                    salida2 = False                
                else:
                    self.clrsrc()
                    input("Ingrese una opción valida")            
            except:
                self.SubGR()
    
    ##menu evaluar cadenas gramaticas
    ## menu evaluar cadenas
    def SubEChainGR(self):        
        print("Lista de las gramaticas cargadas en el sistema.\n")
        for a in range(len(self.boveda)):
            if self.boveda[a].getTipo()=="Gramatica":
                print("-> "+self.boveda[a].getName())
        auto = str(input("\nIngrese el nombre de la gramatica que quiere para validar una cadena: "))
        for i in range(len(self.boveda)):            
            if auto == self.boveda[i].getName() and self.boveda[i].getTipo() =="Gramatica":
                try:
                    print("1- Validar cadena")
                    print("2- Ruta en Gramatica\n")
                    opcion = str(input("Ingrese una opcion: "))
                    if opcion=="1":
                        cadena = str(input("\nIngrese la cadena a evaluar: "))
                        uffff, ruta = self.validarCadenaGR(auto, cadena)
                        #print(self.aceptamos)
                        if uffff == True:
                            input("¡CADENA VALIDA!")
                        else:
                            input("¡CADENA INVALIDA!")
                    elif opcion =="2":
                        #print("saquemos la ruta")
                        cadena = str(input("\nIngrese la cadena a evaluar: "))
                        uffff, ruta = self.validarCadenaGR(auto, cadena)
                        #print(self.aceptamos)
                        if uffff == True:
                            print("¡CADENA VALIDA!")
                        else:
                            print("¡CADENA INVALIDA!")
                        print("Ruta seguida por la gramatica: \n")
                        for z in range(len(ruta)):
                            print(ruta[z])
                        input("\nFin reporte, presione ENTER para continuar.")
                    else:
                        input("Opcion invalida.")
                except:
                    self.SubEChainGR()

    def validarCadenaGR(self, nome,cadena):        
        aceptamos = False
        ruta = []
        bandera = 0        
        final = ""
        #print(cadena.__len__())
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()=="Gramatica":
                #for para la cadena ingresada
                for a in range(cadena.__len__()):
                    #print("empezamos con el for de la cadena")
                    #for para recorrer las transiciones del automata
                    for b in range(len(self.boveda[i].getProducciones())):
                        #print("empezamos con el for de las transiciones")
                        if bandera == 0:
                            if self.boveda[i].getProducciones()[b].gettInicial().getInicio()==True and cadena[a]==self.boveda[i].getProducciones()[b].getTerminal():
                                bandera+=1                                
                                aceptamos = self.boveda[i].getProducciones()[b].gettFinal().getEpsilon()
                                final = self.boveda[i].getProducciones()[b].gettFinal().getName()
                                transicion = self.boveda[i].getProducciones()[b].gettInicial().getName()+","+self.boveda[i].getProducciones()[b].getTerminal()+";"+self.boveda[i].getProducciones()[b].gettFinal().getName()
                                ruta.append(transicion)
                                break
                                #print("aceptacion transicion 1" + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en el inicial")                            
                        else:
                            if final == self.boveda[i].getProducciones()[b].gettInicial().getName() and cadena[a]==self.boveda[i].getProducciones()[b].getTerminal():
                                aceptamos = self.boveda[i].getProducciones()[b].gettFinal().getEpsilon()
                                final = self.boveda[i].getProducciones()[b].gettFinal().getName()
                                transicion = self.boveda[i].getProducciones()[b].gettInicial().getName()+","+self.boveda[i].getProducciones()[b].getTerminal()+";"+self.boveda[i].getProducciones()[b].gettFinal().getName()
                                ruta.append(transicion)
                                break
                                #print("aceptacion transicion " + str(b+1) + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en los demas transiciones")                            
        return aceptamos, ruta

    ## menu evaluar cadenas AFD
    def SubEChainAFD(self):        
        print("Lista de automatas cargados en el sistema.\n")
        for a in range(len(self.boveda)):
            if self.boveda[a].getTipo()=="AFD":
                print("-> "+self.boveda[a].getName())
        auto = str(input("\nIngrese el nombre del automata que quiere para validar una cadena: "))
        for i in range(len(self.boveda)):            
            if auto == self.boveda[i].getName() and self.boveda[i].getTipo() =="AFD":
                try:
                    print("1- Validar cadena")
                    print("2- Ruta en AFD\n")
                    opcion = str(input("Ingrese una opcion: "))
                    if opcion=="1":
                        cadena = str(input("\nIngrese la cadena a evaluar: "))
                        uffff, ruta = self.validarCadenaAFD(auto, cadena)
                        #print(self.aceptamos)
                        if uffff == True:
                            input("¡CADENA VALIDA!")
                        else:
                            input("¡CADENA INVALIDA!")
                    elif opcion =="2":
                        #print("saquemos la ruta")
                        cadena = str(input("\nIngrese la cadena a evaluar: "))
                        uffff, ruta = self.validarCadenaAFD(auto, cadena)
                        #print(self.aceptamos)
                        if uffff == True:
                            print("¡CADENA VALIDA!")
                        else:
                            print("¡CADENA INVALIDA!")
                        print("Ruta seguida por el automata: \n")
                        for z in range(len(ruta)):
                            print(ruta[z])
                        input("\nFin reporte, presione ENTER para continuar.")
                    else:
                        input("Opcion invalida.")
                except:
                    self.SubEChainAFD()

    def validarCadenaAFD(self, nome,cadena):        
        aceptamos = False
        ruta = []
        bandera = 0        
        final = ""
        #print(cadena.__len__())
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()=="AFD":
                #for para la cadena ingresada
                for a in range(cadena.__len__()):
                    #print("empezamos con el for de la cadena")
                    #for para recorrer las transiciones del automata
                    for b in range(len(self.boveda[i].getTransiciones())):
                        #print("empezamos con el for de las transiciones")
                        if bandera == 0:
                            if self.boveda[i].getTransiciones()[b].geteInicial().getInicio()==True and cadena[a]==self.boveda[i].getTransiciones()[b].getEntrada():
                                bandera+=1                                
                                aceptamos = self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()
                                final = self.boveda[i].getTransiciones()[b].geteFinal().getNameE()
                                transicion = self.boveda[i].getTransiciones()[b].geteInicial().getNameE()+","+self.boveda[i].getTransiciones()[b].getEntrada()+";"+self.boveda[i].getTransiciones()[b].geteFinal().getNameE()
                                ruta.append(transicion)
                                break
                                #print("aceptacion transicion 1" + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en el inicial")                            
                        else:
                            if final == self.boveda[i].getTransiciones()[b].geteInicial().getNameE() and cadena[a]==self.boveda[i].getTransiciones()[b].getEntrada():
                                aceptamos = self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()
                                final = self.boveda[i].getTransiciones()[b].geteFinal().getNameE()
                                transicion = self.boveda[i].getTransiciones()[b].geteInicial().getNameE()+","+self.boveda[i].getTransiciones()[b].getEntrada()+";"+self.boveda[i].getTransiciones()[b].geteFinal().getNameE()
                                ruta.append(transicion)
                                break
                                #print("aceptacion transicion " + str(b+1) + str(self.boveda[i].getTransiciones()[b].geteFinal().getAcepta()))
                                #input("pasa en los demas transiciones")                            
        return aceptamos, ruta

        ##cadena minima
    def cadenaMinima(self, nome):                
        cadena=""
        bandera = 0        
        final = ""
        #print(cadena.__len__())
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()=="AFD":
                #for para la cadena ingresada                
                    #print("empezamos con el for de la cadena")
                    #for para recorrer las transiciones del automata
                for b in range(len(self.boveda[i].getTransiciones())):
                        #print("empezamos con el for de las transiciones")
                    if bandera == 0:
                        if self.boveda[i].getTransiciones()[b].geteInicial().getInicio()==True:
                            bandera+=1                                
                            cadena+=self.boveda[i].getTransiciones()[b].getEntrada()
                            final = self.boveda[i].getTransiciones()[b].geteFinal().getNameE()
                            
                    else:
                        if final == self.boveda[i].getTransiciones()[b].geteInicial().getNameE():
                            if True == self.boveda[i].getTransiciones()[b].geteInicial().getAcepta():
                                cadena+=self.boveda[i].getTransiciones()[b].getEntrada()
                                final = self.boveda[i].getTransiciones()[b].geteFinal().getNameE()                            
                                break
                            else:
                                cadena+=self.boveda[i].getTransiciones()[b].getEntrada()
                                final = self.boveda[i].getTransiciones()[b].geteFinal().getNameE()                            
        return cadena

        


    # menu cargar archivo    
    def generarAFD(self,nome):
        for a in range(len(self.boveda)):
            if self.boveda[a].getName()==nome and self.boveda[a].getTipo()=="Gramatica":
                nuevoAFD = Aefede(nome)                
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
                    #inicial
                    estadoInicial = Estado(self.boveda[a].getProducciones()[j].gettInicial().getName())
                    estadoInicial.setAcepta(self.boveda[a].getProducciones()[j].gettInicial().getEpsilon())
                    estadoInicial.setInicio(self.boveda[a].getProducciones()[j].gettInicial().getInicio())
                    estadoInicial.setSalidas(self.boveda[a].getProducciones()[j].gettInicial().getSalidas())
                    estadoInicial.setAlto(self.boveda[a].getProducciones()[j].gettInicial().getAlto())
                    #final
                    estadoFinal = Estado(self.boveda[a].getProducciones()[j].gettFinal().getName())
                    estadoFinal.setAcepta(self.boveda[a].getProducciones()[j].gettFinal().getEpsilon())
                    estadoFinal.setInicio(self.boveda[a].getProducciones()[j].gettFinal().getInicio())
                    estadoInicial.setSalidas(self.boveda[a].getProducciones()[j].gettInicial().getSalidas())
                    estadoInicial.setAlto(self.boveda[a].getProducciones()[j].gettInicial().getAlto())
                    #entrada
                    entrada = self.boveda[a].getProducciones()[j].getTerminal()
                    nuevaTran = Transicion(estadoInicial,estadoFinal,entrada)
                    nuevoAFD.getTransiciones().append(nuevaTran)
                self.boveda.append(nuevoAFD)
    
    def generarGR(self,nome):
        for a in range(len(self.boveda)):
            if self.boveda[a].getName()==nome and self.boveda[a].getTipo()=="AFD":
                nuevaGR= Gramatica(nome)                
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
                    #inicial
                    NTInicial = noTerminal(self.boveda[a].getTransiciones()[j].geteInicial().getNameE())
                    NTInicial.setEpsilon(self.boveda[a].getTransiciones()[j].geteInicial().getAcepta())
                    NTInicial.setInicio(self.boveda[a].getTransiciones()[j].geteInicial().getInicio())
                    NTInicial.setSalidas(self.boveda[a].getTransiciones()[j].geteInicial().getSalidas())
                    NTInicial.setAlto(self.boveda[a].getTransiciones()[j].geteInicial().getAlto())
                    #final
                    NTFinal = noTerminal(self.boveda[a].getTransiciones()[j].geteFinal().getNameE())
                    NTFinal.setEpsilon(self.boveda[a].getTransiciones()[j].geteFinal().getAcepta())
                    NTFinal.setInicio(self.boveda[a].getTransiciones()[j].geteFinal().getInicio())
                    NTFinal.setSalidas(self.boveda[a].getTransiciones()[j].geteFinal().getSalidas())                    
                    NTFinal.setAlto(self.boveda[a].getTransiciones()[j].geteFinal().getAlto())                    
                    #entrada
                    entrada = self.boveda[a].getTransiciones()[j].getEntrada()
                    nuevaProdu = Produccion(NTInicial,NTFinal,entrada)
                    nuevaGR.getProducciones().append(nuevaProdu)
                self.boveda.append(nuevaGR)

    def escribirAFD(self):
        print("Lista de automatas finitos deterministas en el sistema:\n")
        for a in range(len(self.boveda)):
            if self.boveda[a].getTipo()=="AFD":
                print("-> "+self.boveda[a].getName())
        nombre = str(input("\nIngrese el nombre del AFD que quiere guardar: "))                
        archivo = open(nombre+".afd", 'w')
        estados=""
        alfabeto=""
        estadoInicial=""
        estadosAceptacion=""
        #for para recorrer lista general        
        try:
            for i in range(len(self.boveda)):
                if self.boveda[i].getName()==nombre and self.boveda[i].getTipo()=="AFD":
                    #agregando nombre
                    archivo.writelines(self.boveda[i].getName()+"\n")
                    #agregando estados
                    for n in range(len(self.boveda[i].getEstados())):
                        if n>=1:
                            estados+=","+self.boveda[i].getEstados()[n].getNameE()
                        else:
                            estados=self.boveda[i].getEstados()[n].getNameE()
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
                    flag=0
                    for p in range(len(self.boveda[i].getEstados())):
                        if self.boveda[i].getEstados()[p].getAcepta()==True:
                            if flag>=1:
                                estadosAceptacion += ","+self.boveda[i].getEstados()[p].getNameE()
                            else:
                                estadosAceptacion += self.boveda[i].getEstados()[p].getNameE()
                                flag+=1
                    archivo.writelines(estadosAceptacion+"\n")
                    #agregando transiciones                
                    for q in range(len(self.boveda[i].getTransiciones())):                    
                        archivo.writelines(self.boveda[i].getTransiciones()[q].geteInicial().getNameE()+","+self.boveda[i].getTransiciones()[q].getEntrada()+";"+self.boveda[i].getTransiciones()[q].geteFinal().getNameE()+"\n")                    
                    archivo.writelines("%")
                    input("Archivo generado exitosamente.\nRevise la carpeta local.")            
            archivo.close()
            os.system(nombre+".afd")
        except:
            self.escribirAFD()

    def escribirGR(self):
        print("Lista de gramaticas regulares en el sistema:\n")
        for a in range(len(self.boveda)):
            if self.boveda[a].getTipo()=="Gramatica":
                print("-> "+self.boveda[a].getName())
        nombre = str(input("\nIngrese el nombre de la gramatica que quiere guardar: "))        
        archivo = open(nombre+".gre", 'w')
        NoTerms=""
        Termis=""
        NTInicial=""        
        #for para recorrer lista general        
        try:
            for i in range(len(self.boveda)):
                if self.boveda[i].getName()==nombre and self.boveda[i].getTipo()=="Gramatica":
                    #agregando nombre
                    archivo.writelines(self.boveda[i].getName()+"\n")
                    #agregando no terminales
                    for n in range(len(self.boveda[i].getNoTerms())):
                        if n>=1:
                            NoTerms+=","+self.boveda[i].getNoTerms()[n].getName()
                        else:
                            NoTerms=self.boveda[i].getNoTerms()[n].getName()
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
                        archivo.writelines(self.boveda[i].getProducciones()[q].gettInicial().getName()+">"+self.boveda[i].getProducciones()[q].getTerminal()+" "+self.boveda[i].getProducciones()[q].gettFinal().getName()+"\n")
                        if self.boveda[i].getProducciones()[q].gettInicial().getEpsilon()==True:
                            archivo.writelines(self.boveda[i].getProducciones()[q].gettInicial().getName()+">$\n")       
                            self.boveda[i].getProducciones()[q].gettInicial().setAlto(True)
                    archivo.writelines("%")
                    input("Archivo generado exitosamente.\nRevise la carpeta local.")
            archivo.close()
            os.system(nombre+".gre")
        except:
            self.escribirGR()
    #wwwwwwwwwwwwwwwwwwwwwwww
    #eeeeeeeeeeeeeeeeeeeeeeee
    ####alllllltoooooo fin menu guardar                          

    def generarGramaticaConsola(self):
        print("Listando todos los automatas cargados en memoria:\n")
        for i in range(len(self.boveda)):
            if self.boveda[i].getTipo()=="AFD":
                print("->"+self.boveda[i].getName())
        nome = str(input("Ingrese el nombre del AFD para generar la gramatica: "))
        print(" ")
        flag1 = 0
        flag2 = 0
        for a in range(len(self.boveda)):
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()=="AFD":
                for b in range(len(self.boveda)):
                    if nome == self.boveda[a].getName() and self.boveda[a].getTipo()=="Gramatica":
                        #Ya existe no hay que agreagarlo sino mostrarlo
                        flag1+=1
                if flag1==0:
                    #no existe hay que agreagarlo 
                    self.generarGR(nome)
        self.detalleGR(nome)

    def detalleGR(self, nome):
        try:
            for a in range(len(self.boveda)):
                if nome ==self.boveda[a].getName() and self.boveda[a].getTipo()=="Gramatica":
                    #Noterminales
                    print("\nNombre de la Gramatica: " +self.boveda[a].getName())
                    
                    listaNoTerminales=[]
                    for p in range(len(self.boveda[a].getNoTerms())):
                        listaNoTerminales.append(self.boveda[a].getNoTerms()[p].getName())
                    print("\nNo terminales: "+str(listaNoTerminales))
                    #print(listaNoTerminales)
                    #Terminales
                    print("Terminales: "+str(self.boveda[a].getTerminales()))
                    #print(self.boveda[a].getTerminales())
                    #Inicio
                    start=""
                    for i in range(len(self.boveda[a].getNoTerms())):
                        if self.boveda[a].getNoTerms()[i].getInicio()==True:
                            start=self.boveda[a].getNoTerms()[i].getName()
                    print("Estado inicial: "+start)
                    #Producciones
                    print("Producciones:")
                    for z in range(len(self.boveda[a].getProducciones())):
                        print(self.boveda[a].getProducciones()[z].gettInicial().getName()+" > "+self.boveda[a].getProducciones()[z].getTerminal()+" "+self.boveda[a].getProducciones()[z].gettFinal().getName())
                        if self.boveda[a].getProducciones()[z].gettInicial().getEpsilon()==True:
                            print(self.boveda[a].getProducciones()[z].gettInicial().getName()+"> $")
                            self.boveda[a].getProducciones()[z].gettInicial().setAlto(True)
                    input("Fin, Presione Enter para continuar.")
        except:
            self.generarGramaticaConsola()

    def generarHermosoPFD_GR(self):
        try:
            banderaa = 0
            print("Lista de gramaticas regulares en el sistema:\n")
            for a in range(len(self.boveda)):
                if self.boveda[a].getTipo()=="Gramatica":
                    print("-> "+self.boveda[a].getName())
            nome = str(input("\nIngrese el nombre de la gramatica al que le quiere generar el reporte: "))
            nombre = nome+".pdf"
            c = canvas.Canvas(nombre)
            #parte donde agrego los detalles
            titulo = "Nombre: "+nome
            c.setFontSize(20)
            c.drawString(225,750,titulo)                       
            c.setFont('Helvetica', 12)
            for a in range(len(self.boveda)):
                if nome == self.boveda[a].getName() and self.boveda[a].getTipo()=="Gramatica":                                    
                    #añadiendo terminales
                    terminal=""
                    resultado=""
                    for i in range(len(self.boveda[a].getTerminales())):
                        if i >=1:
                            terminal+=", "+self.boveda[a].getTerminales()[i]
                        else:
                            terminal+=self.boveda[a].getTerminales()[i]
                    resultado="Terminales: "+terminal
                    c.drawString(75,700,resultado)
                    #añadiendo no terminales
                    Nt=""
                    resu=""
                    for j in range(len(self.boveda[a].getNoTerms())):
                        if j >=1:                            
                            Nt+=", "+self.boveda[a].getNoTerms()[j].getName()
                        else:
                            Nt+=self.boveda[a].getNoTerms()[j].getName()
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
                    line = int(655)
                    prado=""
                    for l in range(len(self.boveda[a].getProducciones())):
                        line-=15
                        prado=self.boveda[a].getProducciones()[l].gettInicial().getName()+" > "+self.boveda[a].getProducciones()[l].getTerminal()+" "+self.boveda[a].getProducciones()[l].gettFinal().getName()
                        c.drawString(75,line,prado)
                        if self.boveda[a].getProducciones()[l].gettInicial().getEpsilon()==True:
                            line-=15
                            c.drawString(75,line,self.boveda[a].getProducciones()[l].gettInicial().getName()+">$\n")                        
                    for z in range(len(self.boveda)):
                        if nome == self.boveda[z].getName() and self.boveda[z].getTipo()=="AFD":
                            banderaa+=0
                    if banderaa == 0:
                        self.generarAFD(nome)
                    cadena = "Cadena minima de aceptacion: " + self.cadenaMinima(nome)
                    line-=15
                    c.drawString(75,line, cadena)
                    #grafica
                    self.generarDot(nome)
                        #"C:\\Users\\almxo\\Desktop\\"+nome+".dot"
                        #subprocess.call(nome+".dot -Tpng -o "+nome+".png")
                    os.system('dot -Tpng '+nome+'.dot -o '+nome+'.png')
                    pato=nome+".png"                
                    c.drawImage(pato,75,325)
            c.save()
            os.system(nombre)
        except:
            generarHermosoPFD_GR()

    def generarHermosoPFD_AFD(self):
        try:
            print("Lista de automatas finitos deterministas en el sistema:\n")
            for a in range(len(self.boveda)):
                if self.boveda[a].getTipo()=="AFD":
                    print("-> "+self.boveda[a].getName())
            nome = str(input("\nIngrese el nombre del automata al que le quiere generar el reporte: "))
            nombre = nome+".pdf"
            c = canvas.Canvas(nombre)
            #parte donde agrego los detalles        
            titulo = "Nombre: "+nome
            c.setFontSize(20)
            c.drawString(225,750,titulo)                       
            c.setFont('Helvetica', 12)
            for a in range(len(self.boveda)):
                if nome == self.boveda[a].getName() and self.boveda[a].getTipo()=="AFD":                                
                    ##parte del automata               
                    #alfabeto
                    alfa=""
                    for i in range(len(self.boveda[a].getAlfabeto())):
                        if i >=1:                        
                            alfa+=", "+self.boveda[a].getAlfabeto()[i]
                        else:
                            alfa+=self.boveda[a].getAlfabeto()[i]
                    c.drawString(75,700,"Alfabeto:"+alfa)
                    #estados
                    estadio=""
                    for j in range(len(self.boveda[a].getEstados())):
                        if j >=1:
                            estadio+=", "+self.boveda[a].getEstados()[j].getNameE()
                        else:
                            estadio+=self.boveda[a].getEstados()[j].getNameE()
                    c.drawString(75,685,"Estados: "+estadio)
                    #inicial
                    estarto=""
                    for k in range(len(self.boveda[a].getEstados())):
                        if self.boveda[a].getEstados()[k].getInicio()==True:
                            estarto=self.boveda[a].getEstados()[k].getNameE()
                    c.drawString(75,670,"Estado inicial: "+estarto)
                    #estados de aceptación
                    estufa=""
                    bandy = 0
                    for l in range(len(self.boveda[a].getEstados())):
                        if self.boveda[a].getEstados()[l].getAcepta()==True:
                            if bandy>=1:                            
                                estufa+=", "+self.boveda[a].getEstados()[l].getNameE()
                            else:
                                estufa+=self.boveda[a].getEstados()[l].getNameE()
                                bandy+=1
                    c.drawString(75,655,"Estados de aceptación: "+estufa)
                    #añadiendo transiciones
                    c.drawString(75,640,"Transiciones:")
                    line = int(625)
                    prado=""
                    for l in range(len(self.boveda[a].getTransiciones())):
                        line-=15
                        prado=self.boveda[a].getTransiciones()[l].geteInicial().getNameE()+","+self.boveda[a].getTransiciones()[l].getEntrada()+";"+self.boveda[a].getTransiciones()[l].geteFinal().getNameE()
                        c.drawString(75,line,prado)
                    cadena = "Cadena minima de aceptacion: " + self.cadenaMinima(nome)
                    line-=15
                    c.drawString(75,line, cadena)
                    #grafica
                    self.generarDot(nome)
                    #"C:\\Users\\almxo\\Desktop\\"+nome+".dot"
                    #os.system('dot -Tpng archivo.dot -o salida.png')
                    os.system('dot -Tpng '+ nome+'.dot -o '+nome+'.png')
                    #subprocess.call(nome+".dot -Tpng -o "+nome+".png")
                    pato=nome+".png"                
                    c.drawImage(pato,75,325)                                
            c.save()
            os.system(nombre)
        except:
            self.generarHermosoPFD_AFD()
    
    def generarDot(self, nome):
        try:
            archivo = open(nome+".dot", 'w')
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
                        
                        archivo.write(self.boveda[a].getTransiciones()[j].geteInicial().getNameE()+" -> "+self.boveda[a].getTransiciones()[j].geteFinal().getNameE()+" [label=\""+self.boveda[a].getTransiciones()[j].getEntrada()+" \"];\n")
                    archivo.write("}")
            archivo.close()     
        except:
            pass

#ddddddddddddddddddddddddddddd
#222222222222222222222222222222
                 
    def clrsrc(self):
        os.system("cls")

    def AcerdaDe(self):
        print("Lenguajes Formales de Programación \nAuxiliar: Danilo Urias \nSección: B\nLuis Amilcar Morales Xón\n201701059")
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
            if dato != "salir":
                self.CrearAlfabeto(nome,dato)
            else:
                salida = False

    def CrearAlfabeto(self, nome, alfa):
        for a in range(len(self.boveda)):
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()== "AFD":
                #viendo si no ingresamos un alfabeto que ya está como estado
                bandera = 0
                for k in range(len(self.boveda[a].getEstados())):
                    if alfa == self.boveda[a].getEstados()[k].getNameE():
                        bandera+=1
                if bandera==0:
                    #print("podemos ingresar el alfabeto")
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
        flag = 0
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()== "AFD":
                if self.boveda[i].getEstados():                    
                    #busco el nuevo estado
                    for b in range(len(self.boveda[i].getEstados())):
                        if self.boveda[i].getEstados()[b].getNameE()==dato:
                            flag+=1
                            self.boveda[i].getEstados()[b].setInicio(True)
                    if flag==0:                        
                        input("El estado no existe.\nIntente de nuevo.")
                        self.EstadoInicial(nome)
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

    def Epsilon(self,nome,dato):
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo() == "Gramatica":                        
                if self.boveda[i].getNoTerms():                                                
                    for b in range(len(self.boveda[i].getNoTerms())):
                        if self.boveda[i].getNoTerms()[b].getName()==dato:                                                                
                            self.boveda[i].getNoTerms()[b].setEpsilon(True) 
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
        try:
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
        except:
            pass
##gramaticas
##Gramaticas
##Gramaticas
#copia del santo vergueo para un  estado y modificado para un no terminal
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
            if dato != "salir":
                self.CrearTerminales(nome,dato)
            else:
                salida = False

    def CrearTerminales(self,nome,zona4):
        for a in range(len(self.boveda)):
            if nome == self.boveda[a].getName() and self.boveda[a].getTipo()== "Gramatica":
                #viendo si podemos agregar el terminal
                bandera = 0
                for k in range(len(self.boveda[a].getNoTerms())):
                    if zona4 == self.boveda[a].getNoTerms()[k].getName():
                        bandera+=1
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
        flag = 0
        for i in range(len(self.boveda)):
            if nome == self.boveda[i].getName() and self.boveda[i].getTipo()== "Gramatica":
                if self.boveda[i].getNoTerms():                                        
                    for b in range(len(self.boveda[i].getNoTerms())):
                        if self.boveda[i].getNoTerms()[b].getName()==dato:                                                    
                            flag+=1
                            self.boveda[i].getNoTerms()[b].setInicio(True)
                    if flag==0:                                            
                        input("El no terminal no existe.\nIntente de nuevo.")
                        self.NoTerminalInicial(nome)
                else:
                    input("El AFD al que intenta asignar un estado inicial no cuenta con ningun estado todavia.")
    
    #Ingreso de producciones
    #vamo a ver
    def Produu(self, nome):
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
        try:
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
                                final = self.boveda[i].getNoTerms()[b]
                                        #input("final")

                        if flag1!=0 and flag2!=0 and flag3!=0:
                            if banderita==0:                            
                                trancy = Produccion(inicial, final, frag2[0])
                                self.boveda[i].getProducciones().append(trancy)
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
        except:
            pass
        
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
        for a in range(len(divisonAFDS)):
            automata = divisonAFDS[a].split('\n')
            try:
                automata.remove('')
                automata.remove('')
            except:
                pass
            listaAutomatas.append(automata)
        #Ciclo for para empezar a crear objetos Aefede
        for i in range(len(listaAutomatas)):
            try:
                #verificando si el automata que se quiere agregar ya existe
                flag = 0
                for z in range(len(self.boveda)):
                    if listaAutomatas[i][0] == self.boveda[z].getName() and self.boveda[z].getTipo()=="AFD":
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
                    input("AFD cargado correctamente. Presione ENTER.")

                else:
                    input("El AFD que se quiere agregar ya existe en memoria")
            except:
                pass
    
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
        for a in range(len(divisonGRS)):
            automata = divisonGRS[a].split('\n')
            try:
                automata.remove('')
                automata.remove('')
            except:
                pass
            listaGramaticas.append(automata)
        #Ciclo for para empezar a crear objetos NoTerminales
        for i in range(len(listaGramaticas)):
            try:
                #verificando si la gramatica que se quiere agregar ya existe
                flag = 0
                for z in range(len(self.boveda)):
                    if listaGramaticas[i][0] == self.boveda[z].getName() and self.boveda[z].getTipo()=="Gramatica":
                        flag +=1
                if flag == 0: #el automata no existe y lo agregamos
                    #tratamos con el nombre
                    name = str(listaGramaticas[i][0])
                    gramatica = Gramatica(name)
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
                    input("Gramatica cargada correctamente. Presione ENTER")            
                else:
                    input("La gramatica que se quiere agregar ya existe en memoria")
            except:
                pass

    #intento de quitar recursividad.
    def cargarGR_Izquierda(self):
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
        for a in range(len(divisonGRS)):
            automata = divisonGRS[a].split('\n')
            try:
                automata.remove('')
                automata.remove('')
            except:
                pass
            listaGramaticas.append(automata)
        #Ciclo for para empezar a crear objetos NoTerminales
        for i in range(len(listaGramaticas)):
            try:
                #verificando si la gramatica que se quiere agregar ya existe
                flag = 0
                for z in range(len(self.boveda)):
                    if listaGramaticas[i][0] == self.boveda[z].getName() and self.boveda[z].getTipo()=="Gramatica":
                        flag +=1
                if flag == 0: #el automata no existe y lo agregamos
                    #tratamos con el nombre
                    name = str(listaGramaticas[i][0])
                    gramatica = Gramatica(name)
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
                            prod = listaGramaticas[i][m].split('>')
                            #prod =['A','A 0']
                            parte2 = prod[1].split(" ")
                            #parte2=['A','0']
                            if len(parte2)==2:
                                #print()
                                #A>A 0
                                if prod[0]==parte2[0]:
                                    NTNuevo = prod[0]+"prima"
                                    self.CrearNoTerminal(name,NTNuevo)
                                    self.Epsilon(name,NTNuevo)
                                    #A'>0 A'
                                    nuevaProduccion = NTNuevo+">"+parte2[1]+" "+NTNuevo
                                    self.CrearProducciones(name,str(nuevaProduccion))
                            else:
                                #print()
                                #A>0
                                NTnueva = prod[0]+"prima"
                                self.CrearNoTerminal(name,NTnueva)
                                self.Epsilon(name,NTnueva)
                                nuevaProduu = prod[0]+">"+parte2[0]+" "+NTnueva
                                self.CrearProducciones(name,str(nuevaProduu))                            
                    input("Gramatica cargada correctamente. Presione ENTER")            
                else:
                    input("La gramatica que se quiere agregar ya existe en memoria")
            except:
                pass
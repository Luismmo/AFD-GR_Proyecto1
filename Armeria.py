import codecs
#fabrica de aefedes
class Aefede(object):
    def __init__(self, name):        
        self.nombre = name
        self.estados= list()
        self.alfabeto = []
        self.eInicial = None
        self.eAceptacion = []
        self.transiciones = []
        self.tipo = "AFD"
    #getters
    def getName(self):
        return str(self.nombre)
    def getEstados(self):
        return self.estados
    def getAlfabeto(self):
        return self.alfabeto
    def geteInicial(self):
        return self.eInicial
    def geteAceptacion(self):
        return self.eAceptacion
    def getTransiciones(self):
        return self.transiciones
    def getTipo(self):
        return str(self.tipo)
    #setters
    def setName(self, valor):
        self.nombre = valor
    def seteInicial(self, valor):
        self.eInicial = valor
    def setPrede(self,valor):        
        self.ePrede=valor
    def setAlfabeto(self,valor):
        self.alfabeto=valor


class Transicion(object):
    def __init__(self, inicial, final, entra):
        self.eInicial = inicial
        self.eFinal = final
        self.entrada = entra 
    #getters
    def geteInicial(self):
        return self.eInicial
    def geteFinal(self):
        return self.eFinal
    def getEntrada(self):
        return str(self.entrada)

class Estado(object):
    def __init__(self, nombre):
        self.name = nombre
        self.aceptacion = False
        self.inicio = False
        self.salidas= []
    #Getters
    def getNameE(self):
        return str(self.name)
    def getAcepta(self):
        return self.aceptacion
    def getInicio(self):
        return self.inicio
    def getSalidas(self):        
        return self.salidas

    def setSalidas(self,valor):
        self.salidas=valor
    def setAcepta(self, valor):
        self.aceptacion = valor
    def setInicio(self, valor):
        self.inicio = valor
#frontera
#frontera
#fabrica de gramaticas
class Gramatica(object):
    def __init__(self, name):
        self.nombre = name
        self.noTerms = []
        self.terminales = []
        self.NTinicial = None
        self.producciones = []
        self.tipo = "Gramatica"        
    
    #getters
    def getName(self):
        return str(self.nombre)
    def getNoTerms(self):
        return self.noTerms
    def getTerminales(self):
        return self.terminales
    def getNTinicial(self):
        return self.NTinicial
    def getProducciones (self):
        return self.producciones
    def getTipo(self):
        return str(self.tipo)    
    
    #setters
    def setName (self, valor):
        self.nombre= valor
    def setNTinicial(self, valor):
        self.NTinicial = valor
    def setIzquierda(self,valor):
        self.izquierda=valor
    def setPrede(self,valor):
        self.NTprede = valor
    def setTerminales(self,valor):
        self.terminales=valor

class noTerminal(object):
    def __init__(self, nombre):
        self.name = nombre
        self.epsilon = False
        self.inicio = False
        self.salidas = []
    #getters
    def getName(self):
        return str(self.name)
    def getEpsilon(self):
        return self.epsilon
    def getInicio(self):
        return self.inicio
    def getSalidas(self):
        return self.salidas

    def setSalidas(self,valor):
        self.salidas=valor
    def setInicio(self, valor):
        self.inicio=valor
    def setEpsilon(self, valor):
        self.epsilon=valor

class Produccion (object):
    def __init__(self, inicial, final, termi):
        self.tInicial = inicial
        self.tFinal = final
        self.terminal = termi
    #getters
    def gettInicial(self):
        return self.tInicial
    def gettFinal(self):
        return self.tFinal
    def getTerminal(self):
        return self.terminal
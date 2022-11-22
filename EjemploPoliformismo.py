# Ejemplo1

'''class Mujer():

    def Preguntar(self):
        print("Mujer:")
        self.__nombre = input("\tDigita el nombre: ")
        self.__Apellido = input("\tDigita el apellido: ")
        self.__Telefono = int(input("\tDigite el número del teléfono: "))
    
    def Mostrar(self):
        print("\n",self.__nombre,self.__Apellido," y su número del teléfono es: ",self.__Telefono)

class Hombre():

    def Preguntar(self):
        print("Hombre:")
        self.__nombre = input("\tDigita el nombre: ")
        self.__Apellido = input("\tDigita el apellido: ")
        self.__Telefono = int(input("\tDigite el número del teléfono: "))
    
    def Mostrar(self):
        print("\n",self.__nombre,self.__Apellido," y su número del teléfono es: ",self.__Telefono )

def Info(generoy,generox):
    generoy.Preguntar()
    generox.Preguntar()
    generoy.Mostrar()
    generox.Mostrar()

Info(Mujer(),Hombre())'''

#Ejemplo 2

class Tigre():

    def Information(self):
        self.__eat="Su comida está basado en carne"
        self.__weight_max=310
        self.__speed = 65
    
    def Mostrar(self):
        print("Tigre:")
        print("\t",self.__eat," y su peso máximo es de: ",self.__weight_max," con una velocidad de: ",self.__speed," Km/h")

class Caballo():

    def Information(self):
        self.eat= "Su comida está basado en pasto"
        self.weight_max=450
        self.speed = 88
    
    def Mostrar(self):
        print("Caballo:")
        print("\t",self.eat," y su peso máximo es de: ",self.weight_max," con una velocidad de: ",self.speed," Km/h")

def Mostrar_Resultado(Datos1):
    Datos1.Information()
    Datos1.Mostrar()

Mostrar_Resultado(Tigre())
Mostrar_Resultado(Caballo())

# Clase persona
class Persona:
    # Constructor de persona
    def __init__(self, nombre, edad):
        # Atributos
        self.nombre = nombre
        self.edad = edad
        
    # Método: presentacion de persona
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
     
    # Método para mostrar la persona 
    def __str__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

# Crear objeto (instancia)    
persona1 = Persona("LEBA", 200)
print(persona1)
persona1.presentarse()

#----------------------------------------------------------------------------------

# Clase vehículo
class Vehiculo:
    """Constructor: Se ejecuta al crear un auto"""
    def __init__(self, marca, modelo, año):
        # Atributos
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    # Métodos
    
    # Método: Arrancar
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} del año {self.año}, arranca")
       
    # Método: se muestran los datos del vehiculo
    def __str__(self):
        return f"Vehiculo(marca= '{self.marca}', modelo= '{self.modelo}' año= '{self.año}')"

# Objetos (instancias)
vehiculo1 = Vehiculo("Toyota", "Corolla", 2009)
print(vehiculo1)
vehiculo1.arrancar()

#----------------------------------------------------------------------------------

# Clase CuentaBancaria
class CuentaBancaria:
    """Constructor: Se ejecuta al crear una nueva cuenta"""
    def __init__(self, titular, saldo):
        # Atributos
        self.titular = titular
        self.saldo = saldo
    
    # Método: depositar
    def depositar(self, monto):
        self.saldo += monto
        print(f"El titular '{self.titular}' depositó '{monto:,} Gs'")
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"El titular '{self.titular}' retiró '{monto:,} Gs'")
        else:
            print("Saldo insuficiente")
    
    # Método: mostrar datos de la cuenta
    def __str__(self):
        return f"CuentaBancaria(titular='{self.titular}', saldo={self.saldo:,} Gs)"

# Objetos (instancias)
cuenta1 = CuentaBancaria("Leba", 1000000)
print(cuenta1)  # Muestra: CuentaBancaria(titular='Leba', saldo=1,000,000 Gs)
cuenta1.depositar(50000)  # Deposita y actualiza saldo
cuenta1.retirar(20000000)   # Retira si hay saldo
print(cuenta1)  # Saldo actualizado

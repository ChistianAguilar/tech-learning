# Clase padre `Vehiculo` con marca, modelo, año, metodo arrancar()
# Clase hija `Auto` hereda de Vehiculo + atributos num_puertas + metodo tocar_bocina()
# Calse hija `Moto` hereda de Vehivulo + atributos tipo(deportiva/scooter) + metodo hacer_caballito()

# Clase Padre
class Vehiculo:
    # Constructor del padre
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    # Método: arrancar
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} arranca")
    
    # Método: mostrar todos los datos de Vehiculo
    def __str__(self):
        return f"Vehiculo({self.marca} {self.modelo} {self.año})"
    
    
# Clase hija 1: Auto (hereda de vehiculo)
class Auto(Vehiculo): # <-- Se hereda aquí
    # Constructor del hijo
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año) # Llama al constructor del padre
        self.num_puertas = num_puertas # Nuevo atributo
        
    # Métodos
    
    #Método: tocar la bocina
    def tocar_bocina(self):
        print("¡piiii! ¡piii!")
        
    # Método: mostrar todos los datos de Auto
    def __str__(self):
        return f"Auto {super().__str__()}, puertas={self.num_puertas}"
    
# Clase hija 2: Moto
class Moto (Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año) # Llamar al constructor del padre
        self.tipo = tipo
        
    # Métodos
    
    # Método: Hacer caballito
    def hacer_caballito(self):
        print("¡Haciendo caballito!")
    
    # Método: 
    def __str__(self):
        return f"Moto {super().__str__()}, tipo ={self.tipo}"
    
# Objetos (instancias)

mi_auto = Auto("Toyota", "Corolla", 2020, 4)
mi_moto = Moto("Honda", "Navi", 2022, "scooter")

print(mi_auto)
mi_auto.tocar_bocina()
mi_auto.arrancar()

print(mi_moto)
mi_moto.arrancar()
mi_moto.hacer_caballito()

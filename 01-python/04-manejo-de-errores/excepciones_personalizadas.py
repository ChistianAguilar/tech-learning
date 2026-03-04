
# Excepciones personalizadas

# Excepcion básica
print("--- Excepción básica ---")
# Errores de emergencia rapida
try:
    edad = -5
    if edad < 0: 
        raise ValueError("La edad no puede negativa")# Se lanza el error personalizado
except ValueError as e:
    print(f"Error {e}")


print("--- Excepcion intermedia ---")
# Errores mas estandar (reutiliza errores de python)
def crear_usuario(edad):
    if edad < 0:
        raise ValueError ("Edad debe ser positiva") # ValueError nativo
    print("Usuario creado")
try:
    crear_usuario(-4)
except ValueError as e:
    print(f"{e}")
    
    
print("--- Excepción Genérica ---")
# Para errores mas especifico (clase minima)
class SaldoInsuficiente(Exception):
    pass # Clase vacía que hereda Exception

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficiente("No tienes fondos") # La clase
    print("Retiro OK")
    
try:
    retirar(100, 500)
except SaldoInsuficiente:
    print("Sin plata")


print("--- Excepcion Mensaje Personalizado ---")

class SaldoInsuficienteDetallado(Exception):
    def __init__(self, saldo_actual, monto_intentado):
        self.saldo = saldo_actual
        self.monto = monto_intentado
        mensaje = f"Saldo ${self.saldo:,} insuficiente para ${self.monto:,}"
        super().__init__(mensaje)

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteDetallado(saldo, monto)
    print("Retiro OK")

try:
    retirar(1000, 2000)
except SaldoInsuficienteDetallado as e:
    print(f"{e}")
    print(f"Detalles: {e.saldo=}, {e.monto=}")

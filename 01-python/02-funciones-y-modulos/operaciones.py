#------------
# Funciones -
#------------

# Función de suma
def sumar (a, b):
    """Suma dos números y retorna el resulatado"""
    suma = a + b
    return suma


#-----------------------------------------
# Función de resta

def restar (a, b):
    """Resta dos números y retorna el resultado"""
    resta = a - b
    return resta


#-----------------------------------------
# Función de multiplicación

def multiplicar (a, b):
    """Mútiplica dos números y retorna el resutado"""
    mul = a * b
    return mul


#-----------------------------------------
# Función de divición

def dividir (a, b):
    """Dividimos dos numeros y retorna el resultado"""
    # Evitar una divición entre cero
    if b == 0:
        return "Error: no se puede dividir entre cero"

    dividir = a / b
    return dividir


#-----------------------------------------
# Función de potencia

def potencia (base, exponente = 2):
    """Eleva base al exponente, por defecto eleva el cuadrado"""
    return base ** exponente

"""
potencia(2) # Eleva al cuadrado
potencia(2, 2) # Eleva al cubo
"""

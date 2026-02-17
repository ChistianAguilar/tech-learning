# Crear una funcion que retrone un saludo personalizado 

def saludar (nombre):
    """Enviamos un emensaje personalizado"""
    return f"¡Hola {nombre}! ¿Cómo te va?"



#----------------------------------------
# Crear una función que retorne cuantas palabras tiene un texto

def contar_palabras(texto):
    """Lee la cantidad de palabras que tiene el texto"""
    return len(texto.split())



#----------------------------------------
# Crear una función que retorne el texto alrevés

def invertir_texto(texto):
    """Imprime el texto recibido del revés"""
    return texto[::-1]



#----------------------------------------
# Creau una función que retorne el texto en mayúsculas

def mayusculas (texto):
    """Recive el texto y lo transforma en mayúscula"""
    return texto.upper()



#----------------------------------------
# Creau una función que retorne 'True' si el texto es igual al revés

def es_palindromo (texto):
    """Recibe el texto y verifica que se leea del derecho y el revés"""
    texto = texto.lower().replace(" ", "") # Con .replace quitamos los espacions
    return texto == texto[::-1]


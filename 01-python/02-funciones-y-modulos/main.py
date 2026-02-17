import operaciones
import utilidades

print("""
      =====================
      Inicio de Operaciones
      =====================
      ""","\n")
# Operaciones

# Operación sumar
print("Operación 1 - suma")
operacion1 = operaciones.sumar(1, 2)
print(operacion1,"\n")


# Operación resta
print("Operación 2 - resta")
operacion2 = operaciones.restar(3, 5)
print(operacion2,"\n")


# Operación multiplicar
print("Operación 3 - multiplicación")
operacion3 = operaciones.multiplicar(4, 2)
print(operacion3,"\n")


# Operación dividir
print("Operación 4 - división")
operacion4 = operaciones.dividir(10, 2)
print(operacion4,"\n")


# Operación potencia al cuadrado
print("Operación 5 - potencia al cuadrado")
operacion5 = operaciones.potencia(2)
print(operacion5,"\n")


# Operación potencia al cubo
print("Operación 6 - potencia al cubo")
operacion6 = operaciones.potencia(2, 3)
print(operacion6,"\n")


print("Operación 7 - suma y potencia")
operacion7 = operaciones.sumar(1, 3)
print(operaciones.potencia(operacion7),"\n")

print("""
      =====================
      Fin de la operaciones
      =====================
      """)

#-------------------------------------------------------------------


print("""
      =====================
      Inicio de Utilidades
      =====================
      ""","\n")
# Utilidades

# Saludo personalizado 
print("Utilidad 1 - saludar ")
utilidad1 = utilidades.saludar("LEBA")
print(utilidad1 ,"\n")


# Contar cantidad de palabras que hay
print("Utilidad 2 - Contador de palabras")
utilidad2 = utilidades.contar_palabras("Hola, como estan el dia de hoy")
print(utilidad2, "\n")


# Invierte texto
print("Utilidad 3 - Invertir texto")
utilidad3 = utilidades.invertir_texto("Pyton")
print(utilidad3,"\n")


# Convierte texto todo el mayúscualas
print("Utilidad 4 - Convertir a mayúsculas")
utilidad4 = utilidades.mayusculas("Python es lo mejor!")
print(utilidad4,"\n")


# Retorna True si la palabra se lee del derecho y del revéz
print("Utilidad 5 - Saber si es palindromo")
utilidad5 = utilidades.es_palindromo("Ana anina ana")
print(utilidad5,"\n")


# Cuenta la cantidad de palabras que tiene el saludo
print("Utilidad 6 - Contar cuantas palabra tiene el saludo")
utilida6 = utilidades.saludar("Leba")
print(utilida6, f"\nEste saludo contiene {utilidades.contar_palabras(utilida6)} palabras","\n")


# Da vuelta el saludo
print("Utilidad 7 - Dar vuelta el saludo")
utilidad7 = utilidades.saludar("Leva")
print(utilidades.invertir_texto(utilidad7),"\n")


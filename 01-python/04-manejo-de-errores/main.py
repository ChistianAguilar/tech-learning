
# Manejo de ValueError

print("--- Manejo de ValueError ---")

def pedir_numero():
    # El bucle no para hasta que se ingrese un núemro 
    while True:
        # Bloque para menejar errores
        try:
            return int(input("Número: ")) # Pedimos el número 
        except ValueError: # Se evalua el error
            print("¡Solo números!")

numero = pedir_numero()  # Usuario puede poner "abc" → sigue pidiendo
print(f"¡Gracias! {numero}")


# --------------------------------------------------------------------


# Manejo de ZeroDivisionError

print("--- Manejo de ZeroDivisionError ---")

def dividir(a, b):
    # Bloque para el manejo de errores
    try:
        return a / b
    except ZeroDivisionError: # Excepcion en caso de que ingrese un cero o un calculo inesperado
        return "Error: Divición por cero"
  
# objetos (instancia)  
print(dividir(10, 2)) # Pasa de forma correcta
print(dividir(10, 0)) # Activa el ZeroDivisionError


# --------------------------------------------------------------------


# Manejo de IndexError

print("--- Manejo de IndexError ---")

opciones = ["Depositar", "Retirar", "Saldo"] # Lista

# Bloque para el maenjo de errores
try:
    indice = int(input("Opcion (0 - 2): ")) # Se selecciona a que posición se queire acceder
    print(opciones[indice])
except ValueError:
    print("Por favor, ingrese un número válido")
except IndexError: # Se ejecuta si se intenta acceder a una lista que no existe 
    print("Opción inválida. Elija 0, 1 o 2")


# --------------------------------------------------------------------


# Manejo de else y finally

print("--- Manejo de else y finally---")

def dividir_dos(a, b):
    try:
        resultado = a / b  # División directa
    except ZeroDivisionError:
        print("NO se puede dividir por cero")
        return 0
    else:
        print("División perfecta")
        return resultado
    finally:
        print("Calculadora lista")
      
print(dividir_dos(10, 2))      
print(dividir_dos(10, 0))      
       
# --------------------------------------------------------------------

# Manejo de múltiples excepciones

print("--- Manejo de multiples excepciones ---")

def divicion_robusta(a, b):
    try:
        resultado = a / b
        return resultado
    except (ZeroDivisionError, ValueError, TypeError) as e: # Tupla
        print (f"Error: {type(e). __name__}")
        return 0
    else:
        print("Divición echa")
    finally:
        print("Listo")

print(divicion_robusta(10, 2))
print(divicion_robusta(10, 0))


# 1. STRING (Texto)
nombre = "leba"
print(f"Variable: nombre = '{nombre}'")
print(f"Tipo: {type(nombre)}")
print(f"Método upper(): {nombre.upper()}")  # Convierte a mayúsculas
print()

# 2. INT (Entero)
num = 200
print(f"Variable: num = {num}")
print(f"Tipo: {type(num)}")
print(f"Método bit_length(): {num.bit_length()}")  # Cantidad de bits necesarios
print()

# 3. FLOAT (Decimal)
decimal = 1.2
print(f"Variable: decimal = {decimal}")
print(f"Tipo: {type(decimal)}")
print(f"Método is_integer(): {decimal.is_integer()}")  # Verifica si es entero
print()

# 4. BOOL (Booleano)
es_valido = True
print(f"Variable: es_valido = {es_valido}")
print(f"Tipo: {type(es_valido)}")
# Los booleanos heredan métodos de int, pero también podemos usar operaciones lógicas
print(f"Operación 'and': {es_valido and True}")  # Operación lógica
print()

# 5. LIST (Lista)
lista = [10, 20, 30, 40]
print(f"Variable: lista = {lista}")
print(f"Tipo: {type(lista)}")
lista.append(50)  # Agrega un elemento
print(f"Después de append(50): {lista}")
print()

# 6. TUPLE (Tupla - Inmutable)
tupla = (1, 2, 3, 4)
print(f"Variable: tupla = {tupla}")
print(f"Tipo: {type(tupla)}")
print(f"Método count(): {tupla.count(2)}")  # Cuenta ocurrencias
print()

# 7. DICT (Diccionario)
persona = {"nombre": "Chris", "edad": 25}
print(f"Variable: persona = {persona}")
print(f"Tipo: {type(persona)}")
print(f"Método keys(): {list(persona.keys())}")  # Obtiene las claves
print()

# 8. SET (Conjunto)
numeros = {1, 2, 3, 4}
print(f"Variable: numeros = {numeros}")
print(f"Tipo: {type(numeros)}")
numeros.add(5)  # Agrega un elemento
print(f"Después de add(5): {numeros}")



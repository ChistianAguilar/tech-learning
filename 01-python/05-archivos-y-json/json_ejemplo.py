# Paso 1: Crear lista de personas (diccionarios)
personas = [
    {"nombre": "Leba", "edad": 25, "ciudad": "Asunción"},
    {"nombre": "Juan", "edad": 19, "ciudad": "Luque"},
    {"nombre": "Carol", "edad": 21, "ciudad": "San Lorenzo"}  
]

print("Lista creada")
print(personas)
print(f"Tipo: {type(personas)}")
print(f"Longitud: {len(personas)}")


# -------------------------------------------------------------------

# Paso 2: Importar módulo JSON
import json

# Guardar en archivo JSON
with open('persona.json', 'w', encoding='utf-8') as archivo:
    json.dump(personas, archivo, indent=4)
    
print("\n Archivo 'persona.json' Creado")
print("Abrelo con Notpad/VS Code para verlo")

#---------------------------------------------------------------------

# Paso 3: Leer JSON
with open('persona.json', 'r', encoding='utf-8') as archivo:
    personas_leidas =json.load(archivo)
    
print("Lista leída:")
print(personas_leidas)
print(f"¿Igual a original? {personas == personas_leidas}")

#---------------------------------------------------------------------

# Paso 4: Agregar nueva persona (esto dentro de la lista de python)
nueva_persona = {"nombre": "Ana", "edad": 27, "ciudad": "Fernando de la Mora"}

# Agregar a la lista leida

personas_leidas.append(nueva_persona)

print("Lista actualizada:")
print(personas_leidas)
print(f"Nuevas personas: {len(personas_leidas)}")

#---------------------------------------------------------------------

# Paso 5: Guardar lista actualizada

with open('persona.json', 'w', encoding='utf-8') as archivo:
    json.dump(personas_leidas, archivo,indent=4)
    
print("Archivo Actualizado")
print("Abre persona.json -> esta ana?")
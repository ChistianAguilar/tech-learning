
# Escribimos un archivo de texto con varias lineas
print("Texto con varias lineas")
with open("datos.txt", "w", encoding="utf-8") as archivo: # con "w" para sobrescribir 
    # Escribe linea1, linea2, etc. Y agrega un saldo de linea con \n
    archivo.write("Línea1\n")
    archivo.write("Línea2\n")
    archivo.write("Línea3\n")
    archivo.write("Línea4\n")
    archivo.write("Línea5\n")

print("===============================================")
   
# Leer archivo completo
print("Leer archivo y mostrarlo")
with open('datos.txt', 'r', encoding='utf-8') as archivo: # con "r" para leer el archivo
    print(archivo.read()) # .read devuelve todo como un string con \n
    
print("===============================================")
    
# Se agrega nuevas lineas al final
print("Agregar lineas al final")
with open("datos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Línea6 Nueva\n")
    archivo.write("Línea7 Nueva\n")

print("===============================================")

# Enumeración de líneas
print("Enumerar lineas")
with open("datos.txt", "r", encoding="utf-8") as archivo:
    for i, linea in enumerate(archivo.readlines(), 1):
        print(f"{i:2d}. {linea.rstrip()}")
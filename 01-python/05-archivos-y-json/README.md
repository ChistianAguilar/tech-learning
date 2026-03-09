# 05 - Archivos y JSON

## Descripción 

Proyectos para aprender a trabajar con archivos de texto y archivos JSON, una habilidad fundamental para guardar y leer datos.

## Qué aprenderé

- Leer y escribir archivos de texto
- Usar `with open()` para menejos seguro de archivos 
- Trabajar con archivos JSON (Cargar y guardar)
- Diferentes metodos de apertura (r, w, a)
- Serialización y deserialización de datos

## Archivos del proyecto 

- `main.py` - Ejemplos de archivos de texto
- `json_ejemplos.py` - Trabajar con archivos JSON
- `datos.txt` - Archivo de texto generado
- `persona.json` - Archivo JSON generado

## Cómo ejecutar
```bash
uv run main.py
uv run json_ejemplos.py
```

## Conceptos claves

- **open()**: Abre un archivo
- **with**: Contexto que cierra el archivo automáticamente
- **'r'**: Modo lectura (read)
- **'w'**: Modo escritura (write, sobreescribe)
- **'a'**: Modo append (agregar al final)
- **json.dump()**: Guardar datos en JSON
- **json.load()**: Cargar datos desde JSON


# 04 - Manejo de Errores

## Descripción 

Proyecto para aprender y manejar errores y execpciones en Python, evitando que el programa se detenga inesperadamente.

## Qué aprendere 
- Usar try/except para capturar errores 
- Manejar diferentes tipos de excepciones 
- Usar finally para código que siempre se ejecuta
- Crear excepciones personalizadas
- Usar else en bloques try/except

## Archivos del proyecto

- `main.py` - Ejemplos de manejo de errores básicos
- `exceptiones_personalizadas.py`- Crear tus propias excepciones 

## Cómo ejecutar
```bash
uv run main.py
un run excepciones_personalizadas.py
```

## Conceptos claves

- **try**: Intenta ejecutar código que puede fallar
- **except**: Captura el error si ocurre
- **else**: Se ejecuta si NO hubo error
- **finally**: Se ejecuta SIEMPRE (haya o no error)
- **raise**: Lanza una excepción manualmente
- **Exception**: Clase base para todas las excepciones
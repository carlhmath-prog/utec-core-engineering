# Python - Clases y modelo de objetos

Este directorio contiene los ejercicios y scripts desarrollados para el proyecto de Programación Orientada a Objetos en Python de la UTEC.

## Contenido

1. Mi primer cuadrado
Objetivo
Crear tu primera clase en Python.

Instrucciones
Define una clase llamada Square que represente un cuadrado.

Para esta primera versión, la clase no necesita contener ningún atributo ni método.

Ejemplo de uso:

spam@camelot:~/$ cat 0-main.py
#!/usr/bin/env python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

spam@camelot:~/$ ./0-main.py
<class '0-square.Square'>
{}
spam@camelot:~/$ 
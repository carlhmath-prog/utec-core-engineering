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

2. Cuadrado con tamaño
Objetivo
Introducir atributos de instancia.

Instrucciones
Define una clase Square con:

un atributo de instancia privado size
El tamaño debe establecerse cuando se crea el objeto.
¿Por qué size es un atributo privado?

El tamaño es crucial para un cuadrado; muchas cosas dependen de él (cálculo del área, perímetro, etc.), así que tú, como constructor de la clase, debes controlar el tipo y el valor de este atributo. Una forma de tener ese control es mantenerlo privado.

Esto se conoce como el principio de encapsulación.

Ejemplo:

spam@camelot:~/$ cat 1-main.py
#!/usr/bin/env python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

spam@camelot:~/$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
spam@camelot:~/$ 
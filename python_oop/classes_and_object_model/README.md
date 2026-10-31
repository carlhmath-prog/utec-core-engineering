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

3. Validación de tamaño
Objetivo
Asegurar que el estado del objeto sea válido.

Instrucciones
Agrega validaciones al atributo size en la clase Square.

El atributo size debe cumplir con lo siguiente:

debe ser un entero. De lo contrario, lanza una excepción TypeError con el mensaje size must be an integer
debe ser mayor o igual que 0. De lo contrario, lanza una excepción ValueError con el mensaje size must be >= 0
Ejemplo:

spam@camelot:~/$ cat 2-main.py
#!/usr/bin/env python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

spam@camelot:~/$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
spam@camelot:~/$ 
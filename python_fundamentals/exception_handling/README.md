# Exception Handling - Python Fundamentals

Ejercicios enfocados en la robustez del código, manejo de excepciones y programación defensiva en Python.

## Lista de Ejercicios

0. Impresión segura de listas
Escribe una función que imprima x elementos de una lista.

Prototipo: def safe_print_list(my_list=[], x=0):
my_list puede contener cualquier tipo (entero, cadena, etc.)
Todos los elementos deben imprimirse en la misma línea, seguidos de una nueva línea.
x representa el número de elementos a imprimir
x puede ser mayor que la longitud de my_list
Devuelve el número real de elementos impresos
Debes usar try: / except:
No se permite importar ningún módulo
No se permite usar len()
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_list = __import__('safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print(f"elements: {nb_print}")

spam@camelot:~/$ ./main.py
12
nb_print: 2
spam@camelot:~/$ 

1. Impresión segura de enteros
Escribe una función que imprima un entero con "{:d}".format() seguido de una nueva línea.

Prototipo: def safe_print_integer(value):
Si value es un entero, imprímelo y devuelve True.
De lo contrario, devuelve False.
Debes usar try: / except:
No se te permite importar ningún módulo
No se te permite usar type()

2. Impresión segura de listas con manejo de tipos
Escribe una función que imprima los primeros x elementos de una lista.

Prototipo: def safe_print_list_integers(my_list=[], x=0):
Imprime solo enteros.
Omite los elementos que no sean enteros.
Devuelve la cantidad de enteros impresos.
Todos los enteros deben imprimirse en la misma línea, seguidos de un salto de línea.
my_list puede contener cualquier tipo (entero, cadena, etc.)
Debes usar try: / except:
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_list_integers = __import__('safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

spam@camelot:~/$ ./main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
spam@camelot:~/$ 

3. Dividir dos enteros de forma segura
Escribe una función que divida dos enteros.

Prototipo: def safe_print_division(a, b):
Realiza la división dentro de un bloque try.
Si ocurre cualquier otra excepción, imprime "Inside result: None".
Imprime siempre "Inside result: <result>" usando finally.
Devuelve el resultado (o None).
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_division = __import__('safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

spam@camelot:~/$ ./main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
spam@camelot:~/$ 

4. Lanzar una excepción
Escribe una función que lance un TypeError.

Prototipo: def raise_exception():
La función debe lanzar un TypeError.

5. Lanzar un mensaje
Escribe una función que lance un NameError con un mensaje personalizado.

Prototipo: def raise_exception_msg(message=""):
La función debe lanzar un NameError con message.
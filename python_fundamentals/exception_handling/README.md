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


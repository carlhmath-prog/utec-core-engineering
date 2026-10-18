# Python - Estructuras de datos básicas
0. Imprimir una lista de enteros
Instrucción actualizada del proyecto
Escribe una función que imprima todos los enteros de una lista.

Prototipo: def print_list_integer(my_list=[])
Formato: un entero por línea
Puedes asumir que cada elemento de my_list es un entero.
Nota importante:
Se espera que formatee explícitamente los enteros usando :d en tu instrucción print. Aunque tu función funcione correctamente sin ello, la mayoría de las comprobaciones automáticas fallarán si no se usa :d.

Ejemplo de ejecución:
$ cat main.py
#!/usr/bin/env python3
print_list_integer = __import__('print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

$ ./main.py
1
2
3
4
5
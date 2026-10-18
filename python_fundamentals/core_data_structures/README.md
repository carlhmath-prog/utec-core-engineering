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

1. Acceso seguro a un elemento de una lista
Escribe una función que recupere un elemento de una lista como en C.

Prototipo: def element_at(my_list, idx):
Si idx es negativo o está fuera de rango, devuelve None.
En caso contrario, devuelve el elemento en la posición idx.
Ejemplo de ejecución:

$ cat main.py
#!/usr/bin/env python3
element_at = __import__('element_at').element_at

my_list = ["a", "b", "c", "d", "e"]
print(element_at(my_list, 3))
print(element_at(my_list, -1))
print(element_at(my_list, 15))

$ ./main.py
d
None
None

2. Reemplaza un elemento en una lista
Escribe una función que reemplace un elemento de una lista en una posición específica.

Prototipo: def replace_in_list(my_list, idx, element):
Si idx es negativo o está fuera de rango, devuelve la lista original sin cambios.
En caso contrario, reemplaza el elemento en la posición idx por element y devuelve la lista.
Ejemplo de ejecución:

$ cat main.py
#!/usr/bin/env python3
replace_in_list = __import__('replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
print(replace_in_list(my_list, 3, 99))
print(replace_in_list(my_list, 15, 99))

$ ./main.py
[1, 2, 3, 99, 5]
[1, 2, 3, 99, 5]

3. Imprima una matriz de enteros
Escribe una función que imprima una matriz de enteros.

Prototipo: def print_matrix_integer(matrix=[[]]):
matrix es una lista de listas (lista 2D).
Formatea cada fila en su propia línea.
Los valores de una fila deben estar separados por un solo espacio.
Ejemplo de ejecución:

$ cat main.py
#!/usr/bin/env python3
print_matrix_integer = __import__('print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)

$ ./main.py
1 2 3
4 5 6
7 8 9
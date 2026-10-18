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

4. Adición de tuplas
Escribe una función que sume dos tuplas.

Prototipo: def add_tuple(tuple_a=(), tuple_b=()):
Devuelve una nueva tupla con exactamente dos enteros.
Trata los valores faltantes como 0.
Ignora los valores más allá de los dos primeros.
Ejemplo de ejecución:

$ cat main.py
#!/usr/bin/env python3
add_tuple = __import__('add_tuple').add_tuple

print(add_tuple((1, 89), (88, 11)))
print(add_tuple((1, 89), (1, )))
print(add_tuple((1, 89), ()))
print(add_tuple((), ()))

$ ./main.py
(89, 100)
(2, 89)
(1, 89)
(0, 0)

5. Elementos comunes en dos conjuntos
Escribe una función que devuelva un conjunto de elementos comunes en dos conjuntos.

Prototipo: def common_elements(set_1, set_2):
Devuelve un nuevo conjunto que contenga solo los elementos presentes en set_1 y set_2.
Ejemplo de ejecución:

$ cat main.py
#!/usr/bin/env python3
common_elements = __import__('common_elements').common_elements

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
print(sorted(list(common_elements(set_1, set_2))))

$ ./main.py
['C']
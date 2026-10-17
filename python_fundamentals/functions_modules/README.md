# Python - Funciones y modularidad

Este directorio contiene los ejercicios prácticos sobre la definición de funciones, lógica condicional, alcance y modularidad en Python 3 desarrollados para UTEC.

0. es_minúscula
Escribe una función:

def islower(c):
La función debe devolver True si c es una letra minúscula y False en caso contrario.

Restricciones:

No puedes usar métodos integrados de cadenas como .islower().
Debes usar lógica ASCII (ord()).
La función debe devolver un valor booleano.
Ejemplo:

>>> islower('a')
True
>>> islower('A')
False
>>> islower('3')
False

1. A mayúsculas
Escribe una función:

def uppercase(str):
La función debe imprimir la cadena en mayúsculas seguida de una nueva línea.

Restricciones:

No se te permite usar .upper().
Debes usar conversión ASCII (ord() y chr()).
La función debe imprimir el resultado directamente.
La función no devuelve ningún valor.
Ejemplo

>>> uppercase("Holberton")
HOLBERTON

2. Imprime el último dígito
Escribe una función:

def print_last_digit(number):
La función debe:

Imprimir el último dígito de number.
Devolver el valor del último dígito.
El último dígito siempre debe ser positivo.

Ejemplo:

>>> print_last_digit(98)
8
>>> print_last_digit(-1024)
4

4. Ejecución de scripts y comportamiento de importación
Introducción
Hasta ahora, has definido funciones y las has ejecutado dentro del mismo archivo. En esta tarea, analizarás qué cambia cuando las funciones se colocan en un archivo y ese archivo se reutiliza desde otro.

Cuando Python importa un archivo, lo ejecuta de arriba abajo en orden para crear su espacio de nombres. Esto significa que:

Las definiciones de funciones se ejecutan.
Las asignaciones de variables se ejecutan.
Cualquier instrucción en el nivel superior (incluido print) también se ejecuta.
Si la ejecución no se controla, importar un archivo puede provocar un comportamiento no deseado.

El objetivo de esta tarea es:

Observar la diferencia entre ejecutar un archivo directamente e importarlo.
Entender por qué el código de nivel superior se ejecuta durante la importación.
Aprender el papel de if __name__ == "__main__".
Distinguir claramente entre definir comportamiento y ejecutar comportamiento.
Debes observar cuidadosamente el comportamiento antes y después de introducir la protección de ejecución. El cuestionario que sigue a esta tarea evaluará tu comprensión de estos conceptos.

Instrucciones:
Crea dos archivos:

Archivo: simple_add.py

Define una función add(a, b) que devuelva la suma de dos números.
En el nivel superior del archivo (fuera de cualquier función, pero después de la definición), llama a la función e imprime el resultado de:
add(3, 5)
Archivo: test_import.py

Importa simple_add.
Ejecuta python3 test_import.py
Observa qué ocurre.

Luego modifica simple_add.py:

Mueve la llamada a print dentro de:
  if __name__ == "__main__":
Ejecuta de nuevo.

Debes asegurarte de que:

Al ejecutar python3 simple_add.py, se imprima el resultado.
Al ejecutar python3 test_import.py, no se imprima nada.

5. Importar una función simple desde un archivo simple
Escribe un programa que importe la función add() del archivo add_0.py e imprima el resultado de la suma 1 + 2 = 3

def add(a, b):
El programa debe:

Asignar 1 a una variable a.
Asignar 2 a una variable b.
Imprimir:
1 + 2 = 3
Restricciones:

No se te permite usar * para importar.
No se te permite usar __import__.
El programa no debe ejecutarse cuando se importe.

6. Mi primera caja de herramientas
Escribe un programa que importe funciones desde calculator_1.py e imprima el resultado de:

suma
resta
multiplicación
división
Usando:

a = 10
b = 5
Cada operación debe imprimirse en su propia línea.

Restricciones:

No se te permite usar * para importar.
El programa no debe ejecutarse cuando se importe.

7. Todo puede ser importado
Escribe un programa que importe la variable a desde variable_load_5.py e imprima su valor.

Restricciones:

No se permite usar * para importar.
El programa no debe ejecutarse cuando se importe.
Ejemplo:

98

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
Repositorio:

Repositorio GitHub: utec-core-engineering
Directorio: python_fundamentals/functions_modules
Archivo: uppercase.py
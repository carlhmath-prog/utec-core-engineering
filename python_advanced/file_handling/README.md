# Python - Manejo de archivos

Este directorio contiene las soluciones para los ejercicios de manipulación y lectura de archivos en Python, cumpliendo con las buenas prácticas y restricciones requeridas.

## Contenido

0. Leer archivo
Escribe una función que lea un archivo de texto (UTF-8) y lo imprima en stdout:

Prototipo: def read_file(filename=""):
Debes usar la sentencia with
No necesitas gestionar excepciones de file permission ni de file doesn't exist.
No se permite importar ningún módulo
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
read_file = __import__('read_file').read_file

read_file("my_file_0.txt")

spam@camelot:~/$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
spam@camelot:~/$ ./main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
spam@camelot:~/$ 

1. Escribir en un archivo
Escribe una función que escriba una cadena en un archivo de texto (UTF-8) y devuelva el número de caracteres escritos:

Prototipo: def write_file(filename="", text=""):
Debes usar la sentencia with
No necesitas gestionar excepciones de permisos de archivo.
Tu función debe crear el archivo si no existe.
Tu función debe sobrescribir el contenido del archivo si ya existe.
No se permite importar ningún módulo
spam@camelot:~/$ cat 1-main.py
#!/usr/bin/env python3
write_file = __import__('write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

spam@camelot:~/$ ./1-main.py
24
spam@camelot:~/$ cat my_first_file.txt
This School is so cool!
spam@camelot:~/$ 

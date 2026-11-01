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

4. Área de un cuadrado
Objetivo
Implementar métodos de instancia.

Instrucciones
Agrega un método de instancia area(self) a la clase Square que devuelva el área del cuadrado según la longitud de su side.

Ejemplo:

spam@camelot:~/$ cat 3-main.py
#!/usr/bin/env python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

spam@camelot:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
spam@camelot:~/$ 

5. Acceder y actualizar un atributo privado
Objetivo
Implementar acceso controlado a los atributos.

Instrucciones
Añade getters y setters para el atributo size.

El setter debe validar la entrada usando las mismas reglas que antes.

¿Por qué un getter y un setter?

size es un atributo privado. Hicimos eso para asegurarnos de controlar el tipo y el valor. Los métodos getter y setter no son 100% Python, pero sí más orientados a POO. Con ellos, podrás validar la asignación de un atributo privado y también definir cómo estará disponible desde fuera el valor del atributo al obtenerlo: ¿por copia?, ¿por asignación?, etc. Además, añadir la validación de tipo/valor en el setter centralizará la lógica, ya que la harás en un solo lugar.

Asegúrate de leer y entender esto: Getters and Setters: Manage Attributes in Python

spam@camelot:~/$ cat 4-main.py
#!/usr/bin/env python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

spam@camelot:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
spam@camelot:~/$ 

6. Imprimir un cuadrado
Objetivo
Usar el estado del objeto para generar salida.

Instrucciones
Agregua un método de instancia público def my_print(self) que imprima en stdout el cuadrado con el carácter #
Si size es igual a 0, imprime una línea vacía
spam@camelot:~/$ cat 5-main.py
#!/usr/bin/env python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

spam@camelot:~/$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
spam@camelot:~/$ 

7. Imprimir la instancia cuadrada
Objetivo
Controlar cómo se representan los objetos como cadenas.

Instrucciones
Agrega e implementa el método especial:

__str__()
Atributo de instancia privado: position:
propiedad def position(self): para recuperarlo
setter de propiedad def position(self, value): para establecerlo:
position debe ser una tupla de 2 enteros positivos, de lo contrario lanza una excepción TypeError con el mensaje position must be a tuple of 2 positive integer
Instanciación con size opcional y position opcional: def __init__(self, size=0, position=(0, 0)):
Método público de instancia: def my_print(self): que imprime en stdout el cuadrado con el carácter #:
si size es igual a 0, imprime una línea vacía
position debe usarse mediante espacios
Imprimir una instancia de Square debe tener el mismo comportamiento que my_print()
spma@camelot:~/$ cat 6-main.py
#!/usr/bin/env python3
Square = __import__('6-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

spma@camelot:~/$ ./6-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
spma@camelot:~/$ 

8. Clase Rectángulo
Objetivo
Reforzar el modelado de objetos con una segunda clase.

Instrucciones
Define una clase Rectangle con:

Atributo de instancia privado width:

propiedad width(self) para recuperarlo

setter de propiedad width(self, value) para asignarlo.

width debe ser un entero; de lo contrario, lanza una excepción TypeError con el mensaje width must be an integer
si width es menor que 0, lanza una excepción ValueError con el mensaje width must be >= 0
Atributo de instancia privado height:

propiedad height(self) para recuperarlo

setter de propiedad height(self, value) para asignarlo

height debe ser un entero; de lo contrario, lanza una excepción TypeError con el mensaje height must be an integer
si height es menor que 0, lanza una excepción ValueError con el mensaje height must be >= 0
Instanciación con width y height opcionales y valor por defecto de 0. (__init__(self, width=0, height=0))

spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

spam@camelot:~/$ ./main.py
{'_Rectangle__width': 2, '_Rectangle__height': 4}
{'_Rectangle__width': 10, '_Rectangle__height': 3}
spam@camelot:~/$ 
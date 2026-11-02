## Python – Herencia y polimorfismo

# se listan los ejercicios propuestos para este modulo:

0. Introducción a la herencia y el polimorfismo
Objetivo
Este tutorial introduce los conceptos de herencia y polimorfismo mediante un ejemplo guiado.

Paso 1 — Crear una clase padre
Crea un archivo:

0-polymorphism_demo.py
Define la siguiente clase:

#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Some sound"
Esta clase define un comportamiento compartido por todos los animales.

Paso 2 — Crear clases hijas
Crea dos subclases que hereden de Animal.

class Dog(Animal):
    pass

class Cat(Animal):
    pass
Estas clases heredan el método speak() de Animal.

Paso 3 — Crear objetos
Añade el siguiente código:

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
Ejecuta el programa y observa la salida.

Paso 4 — Sobrescribir métodos
Modifica las subclases para que cada animal produzca un sonido diferente.

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
Ejecuta el programa de nuevo.

Aunque se llama al mismo método, cada objeto produce un resultado diferente.

Este comportamiento ilustra el polimorfismo.

Paso 5 — Demostrar el polimorfismo
Modifica el programa:

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())
Cada objeto responde a la misma llamada de método con su propio comportamiento.

Paso 6 — Comprobar relaciones entre clases
Python proporciona herramientas para comprobar relaciones entre clases y objetos.

Ejemplo:

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))

1. Geometría básica
Crea una clase llamada BaseGeometry.

Esta clase representa un concepto fundamental para las figuras geométricas. Define el comportamiento sobre el que otras clases de figuras construirán.

El propósito de esta clase es proporcionar funcionalidad compartida que las subclases puedan reutilizar.

Requisitos
La clase debe incluir los siguientes métodos.

area(self)
Este método representa el área de una figura geométrica.

En esta etapa, la clase base no define cómo debe calcularse el área, porque distintas figuras calculan su área de manera diferente.

En su lugar, este método debe lanzar una excepción que indique que el cálculo no está implementado en esta clase.

Más adelante, las clases que representen figuras específicas proporcionarán su propia implementación de este método.

spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
BaseGeometry = __import__('base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

spam@camelot:~/$ ./main.py
[Exception] area() is not implemented
spam@camelot:~/$ 
integer_validator(self, name, value)
Este método valida que un valor represente un entero positivo válido.

El método debe verificar que:

value sea un entero
value sea mayor que 0
Si value no es un entero, lanza:

TypeError: <name> must be an integer
Si value es menor o igual que 0, lanza:

ValueError: <name> must be greater than 0
El parámetro name debe usarse en los mensajes de error.

spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
BaseGeometry = __import__('base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

spam@camelot:~/$ ./main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
spam@camelot:~/$ 
Por qué importa
La clase BaseGeometry define comportamiento común que puede reutilizarse en múltiples figuras geométricas.

Por ejemplo, validar parámetros numéricos es una tarea que varias clases de figuras necesitarán realizar. En lugar de repetir esta lógica en cada clase, se define una sola vez y se reutiliza mediante la herencia.

El método area() también establece una interfaz compartida: todas las figuras derivadas de esta clase proporcionarán su propia forma de calcular un área.

Repositorio:

Repositorio GitHub: utec-core-engineering
Directorio: python_oop/inheritance
Archivo: base_geometry.py

2. Rectángulo
Crea una clase Rectangle que herede de BaseGeometry.

La clase debe representar un rectángulo definido por su ancho y su altura.

Ambos valores deben validarse usando el validador definido en la clase padre.

Instanciación con width y height: def __init__(self, width, height):
width y height deben ser privados. No hay getter ni setter
width y height deben ser enteros positivos, validados por integer_validator
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Rectangle = __import__('1-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

spam@camelot:~/$ ./main.py
<1-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
spam@camelot:~/$ 
Observación
La lógica de validación no necesita reescribirse en esta clase. En su lugar, se reutiliza desde BaseGeometry.

Esto demuestra reutilización de código a través de la herencia.

3. Rectángulo completo
Extiende la clase Rectangle.

La clase ahora debe incluir:

una implementación del método area()

una representación en cadena legible del rectángulo

Instanciación con width y height: def __init__(self, width, height)::

width y height deben ser privados. Sin getter ni setter

width y height deben ser enteros positivos validados por integer_validator

el método area() debe estar implementado

print() debe imprimir, y str() debe devolver, la siguiente descripción del rectángulo: [Rectangle] <width>/<height>

spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Rectangle = __import__('2-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

spam@camelot:~/$ ./main.py
[Rectangle] 3/5
15
spam@camelot:~/$ 
Observación
En este punto, tu clase Rectangle proporciona una implementación concreta de area().

La clase padre definió que el método debía existir, mientras que la clase Rectangle define cómo se calcula realmente el área.

Otras figuras, como Square, también pueden implementar area().

Como distintos objetos pueden responder a la misma llamada de método con su propia implementación, los programas pueden trabajar con diferentes figuras a través de una interfaz común. Esto es un ejemplo de polimorfismo.

4. Cuadrado #1
Crea una clase Square que herede de Rectangle.

Un cuadrado es un rectángulo especializado en el que el ancho y la altura son iguales.

El constructor debe recibir un solo parámetro que represente el tamaño del cuadrado e inicializar la clase padre en consecuencia.

Instanciación con size: def __init__(self, size)::
size debe ser privado. Sin getter ni setter
size debe ser un entero positivo, validado por integer_validator
El método area() debe implementarse
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Square = __import__('1-square').Square

s = Square(13)

print(s)
print(s.area())

spam@camelot:~/$ ./main.py
[Rectangle] 13/13
169
spam@camelot:~/$ 

5. Cuadrado #2
Extiende la clase Square.

Agrega la representación de cadena apropiada para el cuadrado.

print() debe imprimir, y str() debe devolver, la descripción del cuadrado: [Square] <width>/<height>
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Square = __import__('2-square').Square

s = Square(13)

print(s)
print(s.area())

spam@camelot:~/$ ./2-main.py
[Square] 13/13
169
spam@camelot:~/$ 
Reflexión
Considera el siguiente ejemplo:

shapes = [Rectangle(3, 5), Square(4)]

for shape in shapes:
    print(shape.area())
Aunque los objetos de la lista no sean de la misma clase, el programa puede llamar al mismo método en cada objeto.

Cada clase proporciona su propia implementación de area(), por lo que se realiza el cálculo correcto para cada figura.

Esto ilustra una ventaja importante de la herencia y el polimorfismo: los programas pueden trabajar con objetos relacionados mediante un conjunto compartido de métodos, sin necesidad de conocer la clase exacta de cada objeto.
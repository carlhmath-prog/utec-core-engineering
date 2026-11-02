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
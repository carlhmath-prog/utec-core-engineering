#!/usr/bin/env python3
"""
Módulo 0-polymorphism_demo
Demuestra los conceptos básicos de herencia y polimorfismo en Python.
"""


class Animal:
    """Clase base que representa un animal genérico."""

    def speak(self):
        """Retorna el sonido genérico del animal."""
        return "Some sound"


class Dog(Animal):
    """Clase Dog que hereda de Animal y sobrescribe el método speak."""

    def speak(self):
        """Retorna el ladrido del perro."""
        return "Woof"


class Cat(Animal):
    """Clase Cat que hereda de Animal y sobrescribe el método speak."""

    def speak(self):
        """Retorna el maullido del gato."""
        return "Meow"


if __name__ == "__main__":
    # Creación y prueba de objetos individuales
    dog = Dog()
    cat = Cat()

    print(dog.speak())
    print(cat.speak())

    # Demostración de polimorfismo usando una lista de objetos
    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    # Comprobación de relaciones entre clases y objetos
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))

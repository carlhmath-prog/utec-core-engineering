#!/usr/bin/env python3
"""Este módulo define la clase Square con propiedades getter y setter."""


class Square:
    """Representa un cuadrado con getter y setter para el tamaño."""

    def __init__(self, size=0):
        """Inicializa un cuadrado validando el tamaño."""
        self.size = size

    @property
    def size(self):
        """Recupera el valor actual del tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área actual del cuadrado."""
        return self.__size * self.__size

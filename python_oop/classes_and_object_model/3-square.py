#!/usr/bin/env python3
"""Este módulo define la clase Square con cálculo de área."""


class Square:
    """Representa un cuadrado con validación y área."""

    def __init__(self, size=0):
        """Inicializa un cuadrado validando."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área actual del cuadrado."""
        return self.__size * self.__size

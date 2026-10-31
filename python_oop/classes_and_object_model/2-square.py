#!/usr/bin/env python3
"""Este módulo define la clase Square con validación de tamaño."""


class Square:
    """Representa un cuadrado con validaciones."""

    def __init__(self, size=0):
        """Inicializa un cuadrado validando tamaño."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

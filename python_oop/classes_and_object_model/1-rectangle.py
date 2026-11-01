#!/usr/bin/env python3
"""Este módulo define la clase Rectangle con ancho y alto validados."""


class Rectangle:
    """Representa un rectángulo con validación de ancho y alto."""

    def __init__(self, width=0, height=0):
        """Inicializa un rectángulo con ancho y alto opcionales."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Recupera el valor actual del ancho."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece y valida el ancho del rectángulo."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Recupera el valor actual del alto."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece y valida el alto del rectángulo."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

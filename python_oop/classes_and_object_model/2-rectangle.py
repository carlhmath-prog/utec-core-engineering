#!/usr/bin/env python3
"""Este módulo define la clase Rectangle con área y perímetro."""


class Rectangle:
    """Representa un rectángulo con validaciones, área y perímetro."""

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

    def area(self):
        """Devuelve el área actual del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Devuelve el perímetro actual del rectángulo."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

#!/usr/bin/env python3
"""
Módulo 2-rectangle
Define la clase Rectangle que hereda de BaseGeometry,
implementa el cálculo de área y la representación en cadena.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con validación,

    área y representación en cadena.
    """

    def __init__(self, width, height):
        """Inicializa un rectángulo con ancho y altura."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula y retorna el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Retorna la representación formal y legible."""
        return f"[Rectangle] {self.__width}/{self.__height}"

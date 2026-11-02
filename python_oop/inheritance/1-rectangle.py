#!/usr/bin/env python3
"""
Módulo 1-rectangle
Define la clase Rectangle que hereda de BaseGeometry.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo que hereda de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa un rectángulo con ancho y altura validados."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

#!/usr/bin/env python3
"""
Módulo 1-square
Define la clase Square que hereda de Rectangle.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado especializado que hereda de Rectangle."""

    def __init__(self, size):
        """Inicializa un cuadrado con un tamaño validado."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

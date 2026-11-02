#!/usr/bin/env python3
"""
Módulo 2-square
Define la clase Square que hereda de Rectangle y personaliza su impresión.
"""

Rectangle = __import__('1-rectangle').Rectangle if False else __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado que hereda de Rectangle y define su formato."""

    def __init__(self, size):
        """Inicializa un cuadrado con un tamaño validado."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Retorna la representación formal y legible del cuadrado."""
        return f"[Square] {self.__size}/{self.__size}"

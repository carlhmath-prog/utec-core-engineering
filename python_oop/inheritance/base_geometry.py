#!/usr/bin/env python3
"""
Módulo base_geometry
Define la clase BaseGeometry que sirve como base para figuras geométricas.
"""


class BaseGeometry:
    """Clase base para el manejo y validación de figuras geométricas."""

    def area(self):
        """Método que calcula el área, debe ser implementado en subclases."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que value sea un entero estricto y mayor que 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

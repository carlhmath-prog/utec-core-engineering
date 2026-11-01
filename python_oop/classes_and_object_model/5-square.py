#!/usr/bin/env python3
"""Este módulo define la clase Square con método de impresión."""


class Square:
    """Representa un cuadrado con tamaño, área e impresión."""

    def __init__(self, size=0):
        """Inicializa un cuadrado validando el tamaño."""
        self.size = size

    @property
    def size(self):
        """Recupera el valor actual del tamaño."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida el tamaño."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área actual del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """Imprime en stdout el cuadrado con el carácter #."""
        if self.__size == 0:
            print("")
            return

        rows = ["#" * self.__size for _ in range(self.__size)]
        print("\n".join(rows))

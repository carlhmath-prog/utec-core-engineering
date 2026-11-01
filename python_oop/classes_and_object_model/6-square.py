#!/usr/bin/env python3
"""Este módulo define la clase Square con tamaño, posición e impresión."""


class Square:
    """Representa un cuadrado con tamaño, posición y representación."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con tamaño y posición opcionales."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Recupera el valor actual del tamaño."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Recupera la posición actual del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece y valida la posición del cuadrado."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(type(num) is int for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Devuelve el área actual del cuadrado."""
        return self.__size * self.__size

    def __str__(self):
        """Devuelve la representación en cadena del cuadrado."""
        if self.__size == 0:
            return ""

        result = []
        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            row = " " * self.__position[0] + "#" * self.__size
            result.append(row)

        return "\n".join(result)

    def my_print(self):
        """Imprime en stdout la representación en cadena del cuadrado."""
        print(self)
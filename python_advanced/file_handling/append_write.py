#!/usr/bin/env python3
"""Módulo que contiene una función para añadir texto al final de un archivo."""


def append_write(filename="", text=""):
    """Añade una cadena al final de un archivo de texto (UTF-8) y devuelve

    el número de caracteres añadidos.
    """
    with open(filename, "a", encoding="utf-8") as file:
        added = file.write(text)
        return added

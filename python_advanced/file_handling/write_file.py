#!/usr/bin/env python3
"""Módulo que contiene una función para escribir en archivos de texto."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo de texto (UTF-8) y devuelve

    el número de caracteres escritos.
    """
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
        return written

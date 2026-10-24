#!/usr/bin/env python3
"""Módulo para leer archivos de texto usando la sentencia with."""


def read_file(filename=""):
    """Lee un archivo de texto (UTF-8) y lo imprime en stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

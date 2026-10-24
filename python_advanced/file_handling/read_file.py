#!/usr/bin/env python3


def read_file(filename=""):
    """Lee un archivo de texto (UTF-8) y lo imprime en stdout."""
    with open(filename, encoding="utf-8") as file:
        file.text = file.read()
        print(file.text, end="")

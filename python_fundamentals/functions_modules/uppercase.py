#!/usr/bin/env python3


def uppercase(str):
    """Imprime una cadena en mayúsculas usando conversión ASCII."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
    
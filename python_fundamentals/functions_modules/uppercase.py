#!/usr/bin/env python3


def uppercase(str_input):
    """Imprime una cadena en mayúsculas usando conversión ASCII."""
    result = ""
    for c in str_input:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result)

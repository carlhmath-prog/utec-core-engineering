#!/usr/bin/env python3


def pow(a, b):
    """Devuelve el valor de a elevado a la potencia de b usando un bucle."""
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result

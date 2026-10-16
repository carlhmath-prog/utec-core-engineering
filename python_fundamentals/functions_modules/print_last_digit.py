#!/usr/bin/env python3


def print_last_digit(number):
    """Imprime y devuelve el último dígito positivo de un número."""
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit

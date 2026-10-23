#!/usr/bin/env python3


def safe_print_list_integers(my_list=[], x=0):
    # Inicializamos el contador de enteros impresos
    nb_print = 0


    for i in range(x):
        try:
          
            print("{:d}".format(my_list[i]), end="")
            nb_print += 1
        except (ValueError, TypeError, IndexError):
        
            continue

  
    print()
    return nb_print

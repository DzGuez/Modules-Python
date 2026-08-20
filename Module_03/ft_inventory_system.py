#!/usr/bin/env python3

import sys

def parse_inventory(argumentos: list[str]) -> dict[str, int]:
    """ Convierte los argumentos crudos en un diccionario valido """
    """ Cada argumento debe tener el formato valido, para evitar mensajes de error """
    inventario: dict[str, int] = {}

    for parametro in argumentos:
        partes = parametro.split(":")

        if len(partes) != 2:
            print(f"Error - invalid parameter '{parametro}'")
            continue

        nombre, cantidad_text = partes

        if nombre in inventario:
            print(f"Redundant item '{nmbre' - discarding")
            continue

        try:
            cantidad = int(cantidad_texto)
        except ValueError as error:
            print(f"Quantity error for '{nombre': {error}")
            continue

        inventario.update({nombre: cantidad})

        return inventario




if __name__ == "__main__":
    main()


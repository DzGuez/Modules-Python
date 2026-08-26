#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    """ Ejecuta el intento de leer el archivo indicado por argumento"""
    """ Realiza validaciones y pone mensajes de error en caso de no abrir """
    """ Ademas de cerrar e indicarlo en mensaje"""
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <filename>")
        return

    nombre_archivo = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{nombre_archivo}'")

    try:
        archivo: typing.IO[str] = open(nombre_archivo, "r")
    except OSError as error:
        print(f"Error opening file '{nombre_archivo}': {error}")
        return

    print("---")
    print(archivo.read(), end="")
    print("---")

    archivo.close()
    print(f"File '{nombre_archivo}' closed.")


if __name__ == "__main__":
    main()

#!usr/bin/env python3

import sys
import typing


def leer_archivo(nombre_archivo: str) -> str | None:
    """ Abre, muestra y cierra un archivo de texto"""
    try:
        archivo: typing.IO[str] = open(nombre_archivo, "r")
    except OSError as error:
        print(f"Error opening file '{nombre_archivo}': {error}")
        return None

    print("---\n")
    contenido = archivo.read()
    print(contenido, end="")
    print("\n---")

    archivo.close()
    print(f"File '{nombre_archivo}' closed.")

    return contenido


def cambiar_contenido(contenido: str) -> str:
    """ Agrega un # al final de cada linea del texto"""
    lineas = contenido.splitlines()
    lineas_cambiadas = [linea + "#" for linea in lineas]
    return "\n".join(lineas_cambiadas) + "\n"


def guardar_archivo(nombre_archivo: str, contenido: str) -> None:
    """ Crea o reemplaza un archivo y escribe el contenido que le de"""
    print(f"Saving dato to '{nombre_archivo}'")

    try:
        archivo: typing.IO[str] = open(nombre_archivo, "w")
    except OSError as error:
        print(f"Error opening file '{nombre_archivo}': {error}")
        return

    archivo.write(contenido)
    archivo.close()
    print(f"Data saved in file '{nombre_archivo}'.")


def main() -> None:
    """Ejecuta el programa de datos"""
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <filename>")
        return

    nombre_archivo = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{nombre_archivo}'")

    contenido = leer_archivo(nombre_archivo)
    if contenido is None:
        return

    contenido_cambiado = cambiar_contenido(contenido)

    print("Transform data:")
    print("---\n")
    print(contenido_cambiado, end="")
    print("\n---")

    nombre_destino = input("Enter new file name (or empty): ")

    if nombre_destino == "":
        print("Not saving data.")
        return

    guardar_archivo(nombre_destino, contenido_cambiado)


if __name__ == "__main__":
    main()

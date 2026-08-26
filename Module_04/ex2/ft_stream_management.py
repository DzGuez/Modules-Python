#!/usr/bin/env python3

import sys
from typing import IO


def escribir_error(mensaje: str) -> None:
    """ Escribe un mensaje de error en stderr con el prefijo requerido"""
    sys.stderr.write(f"[STDERR] {mensaje}\n")
    sys.stderr.flush()


def leer_archivo(nombre_archivo: str) -> list[str] | None:
    """ Abre un archivo txt, lee las lineas y las devuelve en lista"""
    """ Si ocurre un error lo muestra """
    try:
        archivo: IO[str] = open(nombre_archivo, "r")
    except OSError as error:
        escribir_error(f"Error opening file '{nombre_archivo}': {error}")
        return None

    lineas: list[str] = archivo.readlines()
    archivo.close()
    return lineas


def mostrar_fragmentos(nombre_archivo: str, lineas: list[str]) -> None:
    """ Imprime las lineas del archivo con formato de fragmentos"""
    print("---\n")
    contador: int = 1
    for linea in lineas:
        contenido: str = linea.rstrip("\n")
        print(f"[FRAGMENT {contador:03d}] {contenido}")
        contador += 1
    print("\n---")
    print(f"File '{nombre_archivo}' closed.\n")


def transformar_lineas(lineas: list[str]) -> list[str]:
    """ Agrega un # al final de cada linea """
    nuevas_lineas: list[str] = []
    for linea in lineas:
        contenido: str = linea.rstrip("\n")
        nuevas_lineas.append(f"{contenido}#\n")
    return nuevas_lineas


def mostrar_fragmentos_cambiados(lineas: list[str]) -> None:
    """ Imprime las lineas cambias con formato de fragmento"""
    print("Transform data:")
    print("---\n")
    contador: int = 1
    for linea in lineas:
        contenido: str = linea.rstrip("\n")
        print(f"[FRAGMENT {contador:03d}] {contenido}")
        contador += 1
    print("\n---")


def leer_nombre_archivo_nuevo() -> str:
    """ Lee un nombre de archivo sin usar input"""
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    entrada: str = sys.stdin.readline()
    return entrada.rstrip("\n")


def guardar_archivo(nombre_archivo: str, lineas: list[str]) -> None:
    """ Intenta guardar las lineas cambiadas en un archivo"""
    print(f"Saving data to '{nombre_archivo}'")

    try:
        archivo: IO[str] = open(nombre_archivo, "w")
    except OSError as error:
        escribir_error(f"Error opening file '{nombre_archivo}': {error}")
        print("Data not saved.")
        return

    for linea in lineas:
        archivo.write(linea)
    archivo.close()


def main() -> None:
    """ Ejecuta el programa """
    if len(sys.argv) != 2:
        escribir_error("Usage: python3 ft_stream_management.py <filename>")
        return

    nombre_archivo: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{nombre_archivo}'")

    lineas: list[str] | None = leer_archivo(nombre_archivo)
    if lineas is None:
        return

    mostrar_fragmentos(nombre_archivo, lineas)

    lineas_cambiadas: list[str] = transformar_lineas(lineas)
    mostrar_fragmentos_cambiados(lineas_cambiadas)

    nombre_destino: str = leer_nombre_archivo_nuevo()
    if nombre_destino == "":
        print("Data not saved.")
        return

    guardar_archivo(nombre_destino, lineas_cambiadas)


if __name__ == "__main__":
    main()

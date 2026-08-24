#!/usr/bin/env python3

""" ft_coordinate_system.py
Sistema de coordenadas 3D. Permite ingresar a posiciones como tuplas (x, y, z)
Y calcular distancias entre puntos"""

import math


def get_player_pos() -> tuple[float, float, float]:
    """ Pide al usuario una posicion y pasa por validaciones"""
    """ Hasta obtener un valor valido."""
    while True:
        enter = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = enter.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coordenadas = []
        error_encontrado = False
        for part in parts:
            try:
                coordenadas.append(float(part))
            except ValueError as error:
                print(f"Error on parameter '{part.strip()}': {error}")
                error_encontrado = True
                break

        if error_encontrado:
            continue

        return (coordenadas[0], coordenadas[1], coordenadas[2])


def main() -> None:
    """Realiza la ejecucion del sistema de coordenadas"""

    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    distancia_centro = math.sqrt(
            first[0] ** 2 + first[1] ** 2 + first[2] ** 2
            )
    print(f"Distance to center: {round(distancia_centro, 4)}")

    print("\nGet a second set of coordinates")
    second = get_player_pos()

    distancia = math.sqrt(
            (second[0] - first[0]) ** 2
            + (second[1] - first[1]) ** 2
            + (second[2] - first[2]) ** 2
            )
    print(f"Distance between the 2 sets of coordinates: {round(distancia, 4)}")


if __name__ == "__main__":
    main()

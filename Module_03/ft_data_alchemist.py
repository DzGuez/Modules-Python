#!usr/bin/env python3

import random

JUGADORES: list[str] = [
        "Alice", "bob", "Charlie", "dylas", "Emma",
        "Gregory", "john", "kevin", "Liam",
        ]


def main() -> None:
    """ Ejecuta la impresion de las listas con los nombres"""

    print("=== Game Data Alchemist ===")
    print(f"\nInitial list of players: {JUGADORES}")

    todos_mayus = [nombre.capitalize() for nombre in JUGADORES]
    print(f"\nNew list with all names capitalized: {todos_mayus}")

    antes_mayus = [nombre for nombre in JUGADORES if nombre[0].isupper()]
    print(f"\nNew list of capitalized names only: {antes_mayus}")

    puntajes = {nombre: random.randint(0, 999) for nombre in todos_mayus}
    print(f"\nScroe dict: {puntajes}")

    promedio = round(sum(puntajes.values()) / len(puntajes), 2)
    print(f"\nScore average is {promedio}")

    puntajes_altos = {
            nombre: puntaje
            for nombre, puntaje in puntajes.items()
            if puntaje > promedio
            }
    print(f"High scores: {puntajes_altos}")


if __name__ == "__main__":
    main()

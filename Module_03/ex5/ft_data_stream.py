#!/usr/bin/env python3

import random
import typing

JUGADORES: list[str] = ["alice", "bob", "charlie", "dylan"]
ACCIONES: list[str] = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "release", "use",
    ]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """ Genera eventos del juego ilimitados, uno a la vez"""
    while True:
        nombre = random.choice(JUGADORES)
        accion = random.choice(ACCIONES)
        yield (nombre, accion)


def consume_event(
        eventos: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    """ Va recorriendo la lista de eventos aleatoriamente """
    """ Al sacarlo de la lista original se modifica con la funcion pop"""
    while len(eventos) > 0:
        indice = random.randrange(len(eventos))
        evento = eventos.pop(indice)
        yield evento


def main() -> None:
    """ Ejecuta la demostracion del sistema"""
    """ Le daremos 1000 eventos para luego generar 10
    para armar una lista."""
    print("=== Game Data Stream Processor ===")

    stream = gen_event()
    for i in range(1000):
        evento = next(stream)
        nombre, accion = evento
        print(f" Event {i}: Player {nombre} did action {accion}")

    generador_lista = gen_event()
    ten_eventos: list[tuple[str, str]] = []
    for _ in range(10):
        ten_eventos.append(next(generador_lista))
    print(f"\nBuilt list of 10 events: {ten_eventos}")

    for evento in consume_event(ten_eventos):
        print(f"\nGot event from list: {evento}")
        print(f"Remains in list: {ten_eventos}")


if __name__ == "__main__":
    main()

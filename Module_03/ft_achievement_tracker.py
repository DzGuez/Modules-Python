#!/usr/bin/env python3

"""ft_achievement_tracker.py
Sistema de seguimiento de logros para varios jugadores usando
sets para garantizar que sean unicos y operar entre conjuntos"""

import random


ACHIEVEMENTS_POOL: list[str] = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder",
        "Night Owl",
        ]

def gen_player_achievements() -> set[str]:
    """ Genera un set aleatorio de los logros para cada jugador"""
    """ Elige una cantidad aleatoria de ellos, sin repetir usando sample()"""
    """ Uso el return para convertirlo en un set ya que sample me da una lista"""
    cantidad_logros = random.randint(6, 10)
    logros_seleccionados = random.sample(ACHIEVEMENTS_POOL, cantidad_logros)
    return set(logros_seleccionados)


def main() -> None:
    """Realiza la ejecucion del sistema de los logros para jugadores"""
    """Genera logros para 4 jugadores y muestra estadisticas de esos logros"""
    print("=== Achievement Tracker System ===")

    jugadores = ["Alice", "Bob", "Charlie", "Dylan"]
    logros_jugadores: dict[str, set[str]] = {}

    for jugador in jugadores:
        logros_jugadores[jugador] = gen_player_achievements()
        print(f"\nPlayer {jugador}: {logros_jugadores[jugador]}")


    todos_los_logros: set[str] = set()
    for logros in logros_jugadores.values():
        todos_los_logros = todos_los_logros.union(logros)
    print(f"\nAll distinct achievements: {todos_los_logros}")


    sets_jugadores = list(logros_jugadores.values())
    comunes = sets_jugadores[0]
    for logros in sets_jugadores[1:]:
        comunes = comunes.intersection(logros)
    print(f"\nCommon achievements: {comunes}\n")


    for jugador in jugadores:
        otros: set[str] = set()
        for otro_jugador, otros_logros in logros_jugadores.items():
            if otro_jugador != jugador:
                otros = otros.union(otros_logros)
        solo_este = logros_jugadores[jugador].difference(otros)
        print(f"Only {jugador} has: {solo_este}")


    for jugador in jugadores:
        faltantes = todos_los_logros.difference(logros_jugadores[jugador])
        print(f"\n{jugador} is missing: {faltantes}")


if __name__ == "__main__":
    main()


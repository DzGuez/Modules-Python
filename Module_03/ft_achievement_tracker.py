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
    """Realiza la ejecucion del sistema de coordenadas"""
    """Genera logros para 4 jugadores y muestra estadisticas de esos logros"""
    print("=== Achievement Tracker System ===")

    jugadores = ["Alice", "Bob", "Charlie", "Dylan"]
    logros_jugadores: dict[str, set[str]] = {}

    

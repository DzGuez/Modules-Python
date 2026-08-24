#!/usr/bin/env python3

""" ft_score_analytics.py
Programa para limpiar datos que ponen jugadores en consola"""

import sys


def main() -> None:
    """ Procesa sys.argv y muestra todo el analisis de puntajes"""

    print("=== Player Score Analytics === ")

    scores = []
    for parameter in sys.argv[1:]:
        try:
            score = int(parameter)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{parameter}'")

    if len(scores) == 0:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total = sum(scores)
    promedio = total / len(scores)
    maximo = max(scores)
    minimo = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {promedio}")
    print(f"High score: {maximo}")
    print(f"Low score: {minimo}")
    print(f"Score range: {maximo - minimo}")


if __name__ == "__main__":
    main()

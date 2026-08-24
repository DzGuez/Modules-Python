#!/usr/bin/env python3

""" ft_command_quest. py
Programa para explorar sys.argv """

import sys


def main() -> None:
    """Mostrar los parametros por linea de comandos"""
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        count = 1
        for parameter in sys.argv[1:]:
            print(f"Argument {count}: {parameter}")
            count += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()

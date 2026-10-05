#!/usr/bin/env python3

import os
import sys


def is_in_virtual_env() -> bool:
    """ Detecta si el script corre dentro de un entorno virtual"""
    return sys.prefix != sys.base_prefix


def show_outside_matrix() -> None:
    """ Muestra el estado cuando no hay entorno virtual activo"""

    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print()
    print("Then run this program again.")


def show_inside_matrix() -> None:
    """ Muestra el estado cuando si hay un entorno virtual activo"""

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")

    venv_path = os.environ.get("VIRTUAL_ENV", "")
    print(f"Virtual Environment: {os.path.basename(venv_path)}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()

    py_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    site_path = os.path.join(sys.prefix, "lib", py_version, "site-packages")
    print("Package installation path:")
    print(site_path)


def main() -> None:

    if is_in_virtual_env():
        show_inside_matrix()
    else:
        show_outside_matrix()


if __name__ == "__main__":
    main()

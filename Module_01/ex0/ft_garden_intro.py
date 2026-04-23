#!/usr/bin/env python3

def garden_info() -> None:
    """ Funcion para crear una planta y mostrar sus caracteristicas """
    name: str = "Rose"
    height: float = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"\nPlant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    garden_info()

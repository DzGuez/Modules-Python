#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """Convierte un string de temperatura en un entero
    Args:
        temp_str: Valor de la temperatura recibida como texto
    Return:
        La temperatura convertida a un entero
    Raises:
        ValueError: En caso de que no se pueda convertir a un numero entero
    """
    return int(temp_str)


def test_temperature() -> None:
    """Realizamos el test de temperatura para 2 escenarios
    sin dejar que el programa termine capturando el error
    """
    print("=== Garden Temperature ===")
    """ pongo los valores en una lista para probar si es valido o no"""
    test_values = ["25", "abc"]

    for value in test_values:
        print(f"\nInput data is '{value}'")
        try:
            """ Intento convertir el dato, si falla va al except """
            """ Lo guardo en una variable para que sea mas facil manejar el dato"""
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}°C")
        except ValueError as e:
            """Como se que sera un error en el valor lo encapsulo con ValueError """
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash! ")


if __name__ == "__main__":
    test_temperature()

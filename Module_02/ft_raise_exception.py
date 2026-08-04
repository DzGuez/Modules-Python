#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """Ahora convierte y vaida una lectura de temperatura para el cultivo
    Tendremos 2 validaciones:
    -El tipo sea convertible a entero
    -El rango de temperatura este entre el minimo y maximo del enunciado
    Args:
        temp_str: Valor de la temperatura recibida como texto
    Return:
        La temperatura que validamos y convertida a un entero
    Raises:
        ValueError: En caso de que no se pueda convertir a un numero entero
        o no este entre el rango (0 - 40)
    """
    temperature = int(temp_str)
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError(f"{temperature}°C is tto cold for plants (min 0°C)")

    return temperature


def test_temperature() -> None:
    """Realizamos el test de temperatura para 4 escenarios
    sin dejar que el programa termine capturando el error"""

    print("=== Garden Temperature Checker ===")
    """ pongo los valores en una lista para probar si es valido o no"""
    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"\nInput data is '{value}'")
        try:
            """ Intento convertir el dato, si falla va al except """
            """ Lo guardo en una variable para un manejo mas facil del dato"""
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}°C")
        except ValueError as e:
            """Como se que sera un error en valor lo encapsulo en ValueError"""
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash! ")


if __name__ == "__main__":
    test_temperature()

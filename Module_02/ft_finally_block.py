#!/usr/bin/env python3

class GardenError (Exception):
    """ Creamos la clase para cualquier tipo de problema del Jardin"""
    """ Y la definimos con un mensaje de error generico"""
    """ Almaceno la excepcion para convertirla a un string """
    def __init__(self, message: str = "Unknow garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """ Creamos la clase para problemas con las plantas """
    """ Que hereda de GardenError """
    def __init__(self, message: str = "Unknow plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """ Funcion para regar una planta si su nombre cumple con requisito"""
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plant_names: list[str]) -> None:
    """ Funcion que prueba el sistema de riego con una lista de plantas"""
    """ Uso la estructura try/except/finally para garantizar que el
    sistema de riego siempre se cierre correctamente """
    try:
        print("Opening watering system")
        for plant in plant_names:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("... ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def watering_plants() -> None:
    """ Es donde empezaremos a regar las plantas para """
    print("=== Garden Watering System ===")

    print("\nTesting valid plants... ")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants... ")
    test_watering_system(["Tomato", "lettuce", "carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    watering_plants()

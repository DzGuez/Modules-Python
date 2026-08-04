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


class WaterError(GardenError):
    """ Creamos la clase para problemas con el agua, regado """
    def __init__(self, message: str = "Unknow water error") -> None:
        super().__init__(message)


class check_plant_health(is_wilting: bool) -> None:
    """ Esta clase verifica el estado de una planta """
    """ y lanza un error si esta mal """
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


class check_water_level(is_empty: bool) -> None:
    """ Esta clase verifica el nivel del agua """
    """ y lanza un error si esta mal """
    if is_empty:
        raise WaterError("Not enough water in the tank!")
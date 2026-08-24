#!/usr/bin/env python3

import sys


def parse_inventory(argumentos: list[str]) -> dict[str, int]:
    """ Convierte los argumentos crudos en un diccionario valido """
    """ Cada argumento debe tener el formato valido, para evitar
    que salgan mensajes de error """
    inventario: dict[str, int] = {}

    for parametro in argumentos:
        partes = parametro.split(":")

        if len(partes) != 2:
            print(f"Error - invalid parameter '{parametro}'")
            continue

        nombre, cantidad_texto = partes

        if nombre in inventario:
            print(f"Redundant item '{nombre}' - discarding")
            continue

        try:
            cantidad = int(cantidad_texto)
        except ValueError as error:
            print(f"Quantity error for '{nombre}': {error}")
            continue

        inventario.update({nombre: cantidad})

    return inventario


def find_extremes(inventario: dict[str, int]) -> tuple[str, int, str, int]:
    """Busca el item mas y menos abundante de todo el inventario"""
    """Use comparaciones con > y < ya que no estan autorizadas las funciones
    max y min """
    claves = list(inventario.keys())
    primero = claves[0]

    mas_abundante = primero
    valor_mas = inventario[primero]
    menos_abundante = primero
    valor_menos = inventario[primero]

    for clave in claves[1:]:
        valor = inventario[clave]
        if valor > valor_mas:
            mas_abundante = clave
            valor_mas = valor
        if valor < valor_menos:
            menos_abundante = clave
            valor_menos = valor

    return mas_abundante, valor_mas, menos_abundante, valor_menos


def main() -> None:
    """Ejecuta el programa del sistema del inventario"""
    print("=== Inventory System Analysis ===")

    inventario = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventario}")

    lista_items = list(inventario.keys())
    print(f"Item list: {lista_items}")

    total = sum(inventario.values())
    print(f"Total quantity of the {len(lista_items)} items: {total}")

    for item in lista_items:
        porcentaje = round(inventario[item] / total * 100, 1)
        print(f"Item {item} represents {porcentaje}%")

    if lista_items:
        mas_nombre, mas_valor, menos_nombre, menos_valor = find_extremes(
                inventario
        )

        print(f"Item most abundant: {mas_nombre} with quantity {mas_valor}")
        print(
            f"Item least abundant: {menos_nombre} with quantity {menos_valor}"
        )

    inventario.update({"magic_item": 1})
    print(f"Updated inventory: {inventario}")


if __name__ == "__main__":
    main()

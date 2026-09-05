#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(dark_ingredients: str) -> str:
    """ Retorna ingredientes validos o invalidos. """
    ing_validos = dark_spell_allowed_ingredients()
    ing_minusculas = dark_ingredients.lower()

    ing_encontrado = False
    for valido in ing_validos:
        if valido.lower() in ing_minusculas:
            ing_encontrado = True
            break

    status = 'VALID' if ing_encontrado else 'INVALID'
    return f"{dark_ingredients} -> {status}"

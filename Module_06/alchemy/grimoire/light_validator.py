#!/usr/bin/env python3

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """ Retorna ingredientes validos o invalidos. """
    ing_validos = light_spell_allowed_ingredients()
    ing_minusculas = ingredients.lower()

    ing_encontrado = False
    for valido in ing_validos:
        if valido.lower() in ing_minusculas:
            ing_encontrado = True
            break

    status = 'VALID' if ing_encontrado else "INVALID"
    return f"{ingredients} - {status}"

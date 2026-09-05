#!/usr/bin/env python3


def light_spell_allowed_ingredients() -> list[str]:
    """ Ingredientes permitidos para el hechizo de luz. """
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """ Registro del hechizo de luz, validado contra los ingredientes """
    from .light_validator import validate_ingredients

    resultado = validate_ingredients(ingredients)
    if "INVALID" in resultado:
        return f"Spell rejected: {spell_name} ({resultado})"
    return f"Spell recorded: {spell_name} ({resultado})"

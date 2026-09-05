#!/usr/bin/env python3

from .dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """ Ingredientes permitidos para el hechizo de oscuridad. """
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_dark_name: str, dark_ingredients: str) -> str:
    """ Registro del hechizo de oscuridad, validado contra los ingredientes """

    resultado = validate_dark_ingredients(dark_ingredients)
    if "INVALID" in resultado:
        return f"Spell reject: {spell_dark_name} with ({resultado})"
    return f"Spell recorded: {spell_dark_name} ({resultado})"

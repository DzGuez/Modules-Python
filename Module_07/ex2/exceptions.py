#!/usr/bin/env python3


class InvalidStrategyError(Exception):
    """ Clase para cualquier tipo de error al seleccionar Creaturas"""
    def __init__(self, message: str) -> None:
        super().__init__(message)

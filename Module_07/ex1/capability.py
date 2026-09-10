#!/usr/bin/env python3

from abc import ABC, abstractmethod


class HealCapability(ABC):
    """ Capacidad abstracta independiente de creature, define curacion"""
    @abstractmethod
    def heal(self) -> str:
        """ Cura a la creatura y retorna un mensaje que lo describe"""
        ...


class TransformCapability(ABC):
    """ Capacidad abstracta independiente de creature, para transformar
    una creatura, siempre tiene un estado si esta tranformado o no."""

    def __init__(self) -> None:
        self._status: bool = False

    @abstractmethod
    def transform(self) -> str:
        """ Activa el estado transformado de la creatura"""
        ...
    
    @abstractmethod
    def revert(self) -> str:
        """ Desactiva el estado transformado de la creatura"""
        ...

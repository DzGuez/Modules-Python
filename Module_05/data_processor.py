#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class para todos los procesadores de datos"""

    def __init__(self) -> None:
        """ Guarda los datos ya convertidos a string en orden de llegada"""
        self._storage: list[tuple[int, str]] = []
        """ Contador total, que llevara la cuenta de todos los items procesado
        en la vida del objeto, nunca se reinicia"""
        self._total_procesados: int = 0
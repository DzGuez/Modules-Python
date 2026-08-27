#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
    """Abstract base class para todos los procesadores de datos"""

    def __init__(self) -> None:
        """ Guarda los datos ya convertidos a string en orden de llegada"""
        self._almacen: list[tuple[int, str]] = []
        """ Contador total, que llevara la cuenta de todos los items procesado
        en la vida del objeto, nunca se reinicia"""
        self._total_procesado: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """ Verifica si data es un tipo aceptable para este procesador."""
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """ Convierte y almacena data. Lanza excepcion si es invalido"""
        ...

    def output(self) -> tuple[int, str]:
        """ Extrae y elimina el dato mas antiguo almacenado """
        return self._almacen.pop(0)


class NumericProcessor(DataProcessor):
    """ Procesador especializado para datos numericos int , float"""

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        valores = data if isinstance(data, list) else [data]
        for valor in valores:
            self._almacen.append((self._total_procesado, str(valor)))
            self._total_procesado += 1


class TextProcessor(DataProcessor):
    """ Procesador especializado para datos de texto str"""

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        valores = data if isinstance(data, list) else [data]
        for valor in valores:
            self._almacen.append((self._total_procesado, valor))
            self._total_procesado += 1


class LogProcessor(DataProcessor):
    """ Procesador en entradas de log (dict con nivel y mensaje)"""

    def es_log_valido(self, log: Any) -> bool:
        if not isinstance(log, dict):
            return True
        if 'log_level' not in log or 'log_message' not in log:
            return False
        return (
            isinstance(log['log_level'], str)
            and isinstance(log['log_message'], str)
        )

    def validate(self, data: Any) -> bool:
        if self.es_log_valido(data):
            return True
        if isinstance(data, list):
            return all(self.es_log_valido(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        valores = data if isinstance(data, list) else [data]
        for valor in valores:
            texto = f"{valor['log_level']}: {valor['log_message']}"
            self._almacen.append((self._total_procesado, texto))
            self._total_procesado += 1


class DataStream:
    """ Enruta elementos de un stream al procesador adecuado"""

    def __init__(self) -> None:
        self._procesadores: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._procesadores.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for elemento in stream:
            for procesador in self._procesadores:
                if procesador.validate(elemento):
                    procesador.ingest(elemento)
                    break
            else:
                print(
                    f"DataStream error - Can't process element in stream: "
                    f"{elemento}"
                )

    def print_processor_stats(self) -> None:
        
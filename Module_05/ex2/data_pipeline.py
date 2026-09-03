#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol
import typing


class ExportPlugin(Protocol):
    """ Molde para cualquier plugin de exportacion debe tener este metodo"""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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

    def get_stats(self) -> tuple[int, int]:
        """ Retorna total procesado historicamente,
        y cantidad pediente por extraer"""
        return (self._total_procesado, len(self._almacen))


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
        print("\n== DataStream statistics ==")
        if not self._procesadores:
            print("Not processor found, no data")
            return

        for procesador in self._procesadores:
            nombre = procesador.__class__.__name__.replace(
                "Processor", " Processor")
            total, restantes = procesador.get_stats()
            print(
                f"{nombre}: total {total} items processed, "
                f"remainig {restantes} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for procesador in self._procesadores:
            resultados: list[tuple[int, str]] = []
            for _ in range(nb):
                resultados.append(procesador.output())
                plugin.process_output(resultados)


class CSVPlugin():
    """ Plugin para exportar y formatear los datos como una linea CSV"""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        textos: list[str] = []
        for rango, valor in data:
            textos.append(valor)

        linea_csv = ",".join(textos)
        print(f"CSV Output:\n{linea_csv}")


class JSONPlugin():
    """ Plugin para exportar y formatear los datos tipo JSON"""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        textos: list[str] = []
        for rango, valor in data:
            textos.append(f'"item_{rango}": "{valor}"')

        cuerpo = ", ".join(textos)
        linea_json = "{" + cuerpo + "}"
        print(f"JSON Output:\n{linea_json}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processor_stats()

    print("\nRegistering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    batch: list[Any] = [
            "Hello world",
            [3.14, -1, 2.71],
            [
                {
                    'log_level': 'WARNING',
                    'log_message': 'Telnet access! Use ssh instead'
                },
                {'log_level': 'INFO', 'log_message': 'User wil is connected'}
            ],
            42,
            ["Hi", "five"]
        ]
    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processor_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    plugin_csv = CSVPlugin()
    stream.output_pipeline(3, plugin_csv)
    stream.print_processor_stats()

    batch_2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE', 'log_message':
                'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print(f"\nSend another batch of data: {batch_2}")
    stream.process_stream(batch_2)
    stream.print_processor_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    plugin_json = JSONPlugin()
    stream.output_pipeline(5, plugin_json)
    stream.print_processor_stats()


if __name__ == "__main__":
    main()

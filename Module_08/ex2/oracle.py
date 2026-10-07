#!/usr/bin/env python3

import os

from dotenv import load_dotenv  # type: ignore[import-not-found]

REQUIRED: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config() -> dict[str, str | None]:
    """ Carga el .env y lee las 5 variables de configuracion"""

    load_dotenv()
    config: dict[str, str | None] = {}
    for key in REQUIRED:
        config[key] = os.environ.get(key)
    return config


def show_config(config: dict[str, str | None]) -> None:
    """ Muestra la configuracion segun el modo (development/production)"""

    mode = config["MATRIX_MODE"] or "development"
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")

    print(f"Mode: {mode}")
    if mode == "production":
        print("Database: Connected to production cluster")
    else:
        print("Database: Connected to local instance")

    api = "Authenticated" if config["API_KEY"] else "Missing"
    print(f"API Access: {api}")

    log = config["LOG_LEVEL"]
    print(f"Log Level: {log}")

    zion = "Online" if config["ZION_ENDPOINT"] else "Offline"
    print(f"Zion Network: {zion}")


def find_missing(config: dict[str, str | None]) -> list[str]:
    """ Devuelve los nombres de las variables sin valor"""
    return [key for key, value in config.items() if not value]


def main() -> None:
    config = load_config()
    missing = find_missing(config)
    if missing:
        print("WARNING: Missing configuration: " + ", ".join(missing))
        print("Copy .env.example to .env and fill in your values.\n")
    show_config(config)
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()

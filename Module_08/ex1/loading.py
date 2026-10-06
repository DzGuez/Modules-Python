#!/usr/bin/env python3

from importlib import import_module, metadata
from typing import Any

PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}


def check_package(name: str, description: str) -> bool:
    """ Indica si un paquete esta instalado, e imprime el estado"""
    try:
        import_module(name)
        version = metadata.version(name)
        print(f"[OK] {name} ({version}) - {description}")
        return True
    except ImportError:
        print(f"[MISSING] {name} - {description}")
        return False


def check_all() -> bool:
    """ Comprueba todos los paquetes. Da True si estan todos"""
    print("Checking dependencies:")
    results: list[bool] = []
    for name, desc in PACKAGES.items():
        ok = check_package(name, desc)
        results.append(ok)
    return all(results)


def run_analysis() -> Any:
    """ Genera datos simulados con numpy y los analiza con pandas"""
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore

    print("\nAnalyzing Matrix data...")
    rng = np.random.default_rng(42)
    data = rng.normal(50, 10, 1000)
    print(f"Processing {len(data)} data points...")
    table = pd.DataFrame({"activity": data})
    return table


def create_visualization(table: Any) -> None:
    """ Dibuja los datos con matplotlib y guarda la imagen"""
    # import matplotlib
    # matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # type: ignore

    print("Generating visualization...")
    plt.figure(figsize=(8, 4))
    plt.plot(table["activity"])
    plt.title("Matrix activity")
    plt.xlabel("Measurement")
    plt.ylabel("Activity")
    plt.savefig("matrix_analysis.png")
    plt.close()


def show_install_help() -> None:
    """ Muestra como instalar las dependencias con pip o Poetry"""
    print("\nMissing dependencies, cannot continue.")
    print()
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("  python3 loading.py")
    print()
    print("Install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    if not check_all():
        show_install_help()
        return
    table = run_analysis()
    create_visualization(table)
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()

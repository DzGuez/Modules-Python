#!/usr/bin/env python3


def secure_archive(
        nombre_archivo: str,
        accion: str = "read",
        contenido: str = "",
        ) -> tuple[bool, str]:
    """ Accede de forma segura a un archivo, para leer o escribir"""
    """ En este caso si usare el with para garantizar el cierre del
    archivo que abra, no importa si hay un error"""
    try:
        if accion == "read":
            with open(nombre_archivo, "r") as archivo:
                datos = archivo.read()
            return (True, datos)

        if accion == "write":
            with open(nombre_archivo, "w") as archivo:
                archivo.write(contenido)
            return (True, "Content successfully written to file")

        return (False, f"Unknown action '{accion}'")

    except OSError as error:
        return (False, str(error))


def main() -> None:
    """ Demuestra los casos para cuando se abre un archivo"""
    print("=== Cyber Archives Security ===")

    resultado = secure_archive("/not/esisting/file")
    print(
        "\nUsing 'secure_archive' to read from a nonexistent file: "
        f"\n{resultado}"
    )

    resultado = secure_archive("/etc/shadow")
    print(
        "\nUsing 'secure_archive' to read from an inaccessible file: "
        f"\n{resultado}"
    )

    resultado = secure_archive("ancient_fragment.txt")
    print(
        "\nUsing 'secure_archive' to read from a regular file: "
        f"\n{resultado}"
    )

    exito, contenido = resultado
    if exito:
        resultado_escritura = secure_archive(
            "new_vault_copy.txt", "write", contenido
        )
        print(
            "\nUsing 'secure_archive' to write previous content to a "
            f"new file: \n{resultado_escritura}"
        )


if __name__ == "__main__":
    main()

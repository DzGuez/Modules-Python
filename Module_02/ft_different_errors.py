#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    """Simula los varios tipos de fallos que podrian ocurrir"""
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        result = 1 / 0
    elif operation_number == 2:
        file = open("/Campus42/Modules_python/error_archivo")
    elif operation_number == 3:
        result = "42Barcelona" + 42
    else:
        return

def test_error_types() -> None:
    """Realiza cada prueba a cada tipo de error de la funcion anterior"""
    print("=== Garden Error Types Demo ===")
    test_operations = [0, 1, 2, 3, 4]

    for operation_number in test_operations:
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
            # Si no hay excepcion, la operacion fue exitosa
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            # Realizo un except con todos los errores para no repetir codigo
            print(f"Caught {e.__class__.__name__}: {e}")
    
    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()

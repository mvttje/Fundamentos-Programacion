
def menu():
    print("=== Menu ===")
    print("1. Agregar alumno")
    print("2. Buscar alumno")
    print("3. Eliminar alumno")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar alumnos")
    print("6. Salir")
    while True:
            try:
                op = int(input("Opcion: "))
                if op >= 1:
                    print("Opcion valida")
                    break
                else:
                    print("Pon un numero entero")
            except ValueError:
                print("Pon un numero entero")
while True:
     menu()




def menu():
    print("=== Menu ===")
    print("1. Agregar jugador")
    print("2. Buscar jugador")
    print("3. Eliminar jugador")
    print("4. Actualizar titularidad")
    print("5. Mostrar jugadores")
    print("6. Salir")

def op():
     while True:
        try:  
            opc = int(input("Opcion: "))
            if opc >= 1:
                print("Opcion valida")
                break
            else:
                print("Opcion invalida, debes poner un numero entero")
        except ValueError:
            print("Opcion invalida, debes poner un numero entero")
while True:
    menu()
    op()


  




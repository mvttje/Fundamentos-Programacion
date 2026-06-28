
vehiculos = []

# ==========================
# FUNCIONES DEL MENÚ
# ==========================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opción entre 1 y 6.")
        except:
            print("Debe ingresar un número entero.")


# ==========================
# FUNCIONES DE VALIDACIÓN
# ==========================

def validar_modelo(modelo):
    return modelo.strip() != ""


def validar_anio(anio):
    return anio > 1900


def validar_precio(precio):
    return precio > 0


# ==========================
# FUNCIONES PRINCIPALES
# ==========================

def agregar_vehiculo(lista):
    modelo = input("Ingrese modelo: ")

    if not validar_modelo(modelo):
        print("Error: El modelo no puede estar vacío.")
        return

    try:
        anio = int(input("Ingrese año: "))
        if not validar_anio(anio):
            print("Error: El año debe ser mayor a 1900.")
            return
    except:
        print("Error: Debe ingresar un número entero para el año.")
        return

    try:
        precio = float(input("Ingrese precio: "))
        if not validar_precio(precio):
            print("Error: El precio debe ser mayor a 0.")
            return
    except:
        print("Error: Debe ingresar un valor numérico para el precio.")
        return

    vehiculo = {
        "modelo": modelo,
        "anio": anio,
        "precio": precio,
        "disponible": False
    }

    lista.append(vehiculo)
    print("Vehículo registrado correctamente.")


def buscar_vehiculo(lista, modelo):
    for i in range(len(lista)):
        if lista[i]["modelo"] == modelo:
            return i
    return -1


def eliminar_vehiculo(lista):
    modelo = input("Ingrese el modelo a eliminar: ")

    posicion = buscar_vehiculo(lista, modelo)

    if posicion != -1:
        lista.pop(posicion)
        print("Vehículo eliminado correctamente.")
    else:
        print(f"El vehículo '{modelo}' no se encuentra registrado.")


def actualizar_disponibilidad(lista):
    for vehiculo in lista:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False


def mostrar_vehiculos(lista):
    actualizar_disponibilidad(lista)

    if len(lista) == 0:
        print("No hay vehículos registrados.")
        return

    print("\n=== LISTA DE VEHÍCULOS ===")

    for vehiculo in lista:
        estado = "DISPONIBLE" if vehiculo["disponible"] else "NO DISPONIBLE"

        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Año: {vehiculo['anio']}")
        print(f"Precio: {vehiculo['precio']}")
        print(f"Estado: {estado}")
        print("*" * 45)


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_vehiculo(vehiculos)

    elif opcion == 2:
        modelo = input("Ingrese el modelo a buscar: ")

        posicion = buscar_vehiculo(vehiculos, modelo)

        if posicion != -1:
            print("\nVehículo encontrado:")
            print(f"Posición: {posicion}")
            print(f"Modelo: {vehiculos[posicion]['modelo']}")
            print(f"Año: {vehiculos[posicion]['anio']}")
            print(f"Precio: {vehiculos[posicion]['precio']}")
            print(f"Disponible: {vehiculos[posicion]['disponible']}")
        else:
            print("Vehículo no encontrado.")

    elif opcion == 3:
        eliminar_vehiculo(vehiculos)

    elif opcion == 4:
        actualizar_disponibilidad(vehiculos)
        print("Disponibilidad actualizada.")

    elif opcion == 5:
        mostrar_vehiculos(vehiculos)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        break
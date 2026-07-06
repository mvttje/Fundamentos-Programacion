
"""
FlorExpress - Sistema de administración de catálogo de arreglos florales y stock.
"""

# ==========================================================
# DATOS INICIALES
# ==========================================================

arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}


# ==========================================================
# FUNCIONES DE VALIDACIÓN (opción 4 - Agregar arreglo)
# ==========================================================

def validar_codigo(codigo):
    if codigo is None or codigo.strip() == "":
        return False
    codigo_upper = codigo.strip().upper()
    claves_existentes = [c.upper() for c in arreglos.keys()]
    return codigo_upper not in claves_existentes


def validar_nombre(nombre):
    return nombre is not None and nombre.strip() != ""


def validar_tipo(tipo):
    return tipo is not None and tipo.strip() != ""


def validar_color(color_principal):
    return color_principal is not None and color_principal.strip() != ""


def validar_tamano(tamano):
    return tamano is not None and tamano.strip() in ('S', 'M', 'L')


def validar_incluye_tarjeta(valor):
    return valor is not None and valor.strip().lower() in ('s', 'n')


def validar_temporada(temporada):
    return temporada is not None and temporada.strip() != ""


def validar_precio(precio):
    try:
        return int(precio) > 0
    except (ValueError, TypeError):
        return False


def validar_unidades(unidades):
    try:
        return int(unidades) >= 0
    except (ValueError, TypeError):
        return False


# ==========================================================
# FUNCIONES PRINCIPALES DEL SISTEMA
# ==========================================================

def unidades_tipo(tipo):
    """Muestra el total de unidades disponibles para un tipo de arreglo dado."""
    total = 0
    tipo_buscado = tipo.strip().lower()
    for codigo, datos in arreglos.items():
        if datos[1].strip().lower() == tipo_buscado:
            if codigo in bodega:
                total += bodega[codigo][1]
    print(f"El total de unidades disponibles es: {total}")


def busqueda_precio(p_min, p_max):
    """Muestra los arreglos con precio dentro de un rango y con unidades disponibles."""
    resultados = []
    for codigo, datos in bodega.items():
        precio = datos[0]
        unidades = datos[1]
        if p_min <= precio <= p_max and unidades != 0:
            if codigo in arreglos:
                nombre = arreglos[codigo][0]
                resultados.append(f"{nombre}--{codigo}")

    if not resultados:
        print("No hay arreglos en ese rango de precios.")
    else:
        resultados.sort()
        print(f"Los arreglos encontrados son: {resultados}")


def actualizar_precio(codigo, nuevo_precio):
    """Actualiza el precio de un arreglo existente. Retorna True/False."""
    for clave in bodega.keys():
        if clave.upper() == codigo.strip().upper():
            bodega[clave][0] = nuevo_precio
            return True
    return False


def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano,
                     incluye_tarjeta, temporada, precio, unidades):
    """Agrega un nuevo arreglo a ambos diccionarios. Retorna True/False."""
    claves_existentes = [c.upper() for c in arreglos.keys()]
    if codigo.strip().upper() in claves_existentes:
        return False

    arreglos[codigo] = [nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada]
    bodega[codigo] = [precio, unidades]
    return True


def eliminar_arreglo(codigo):
    """Elimina un arreglo de ambos diccionarios. Retorna True/False."""
    clave_encontrada = None
    for clave in arreglos.keys():
        if clave.upper() == codigo.strip().upper():
            clave_encontrada = clave
            break

    if clave_encontrada is None:
        return False

    del arreglos[clave_encontrada]
    if clave_encontrada in bodega:
        del bodega[clave_encontrada]
    return True


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")


def opcion_1():
    tipo = input("Ingrese tipo de arreglo a consultar: ")
    unidades_tipo(tipo)


def opcion_2():
    while True:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue

        if p_min < 0 or p_max < 0 or p_min > p_max:
            print("Debe ingresar valores enteros")
            continue

        busqueda_precio(p_min, p_max)
        break


def opcion_3():
    continuar = "s"
    while continuar == "s":
        codigo = input("Ingrese código del arreglo: ")

        while True:
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if nuevo_precio <= 0:
                    print("Debe ingresar un valor entero positivo")
                    continue
                break
            except ValueError:
                print("Debe ingresar un valor entero positivo")

        if actualizar_precio(codigo, nuevo_precio):
            print("Precio actualizado")
        else:
            print("El código no existe")

        continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()


def opcion_4():
    codigo = input("Ingrese código del arreglo: ")
    if not validar_codigo(codigo):
        print("Código inválido o ya existente")
        return

    nombre = input("Ingrese nombre: ")
    if not validar_nombre(nombre):
        print("El nombre no puede estar vacío")
        return

    tipo = input("Ingrese tipo: ")
    if not validar_tipo(tipo):
        print("El tipo no puede estar vacío")
        return

    color_principal = input("Ingrese color principal: ")
    if not validar_color(color_principal):
        print("El color principal no puede estar vacío")
        return

    tamano = input("Ingrese tamaño (S/M/L): ")
    if not validar_tamano(tamano):
        print("El tamaño debe ser 'S', 'M' o 'L'")
        return

    incluye_tarjeta_str = input("¿Incluye tarjeta? (s/n): ")
    if not validar_incluye_tarjeta(incluye_tarjeta_str):
        print("Debe ingresar 's' o 'n'")
        return
    incluye_tarjeta = incluye_tarjeta_str.strip().lower() == 's'

    temporada = input("Ingrese temporada: ")
    if not validar_temporada(temporada):
        print("La temporada no puede estar vacía")
        return

    precio_str = input("Ingrese precio: ")
    if not validar_precio(precio_str):
        print("El precio debe ser un entero mayor que cero")
        return

    unidades_str = input("Ingrese unidades: ")
    if not validar_unidades(unidades_str):
        print("Las unidades deben ser un entero mayor o igual a cero")
        return

    if agregar_arreglo(codigo, nombre, tipo, color_principal, tamano.strip(),
                        incluye_tarjeta, temporada, int(precio_str), int(unidades_str)):
        print("Arreglo agregado")
    else:
        print("El código ya existe")


def opcion_5():
    codigo = input("Ingrese código del arreglo a eliminar: ")
    if eliminar_arreglo(codigo):
        print("Arreglo eliminado")
    else:
        print("El código no existe")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            opcion_4()
        elif opcion == "5":
            opcion_5()
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida")


if __name__ == "__main__":
    main()


# ==========================
# FLORERÍA FLOREXPRESS
# ==========================

# Diccionario con la información de los arreglos
arreglos = {
    "FLO1": ["Ramo Primavera", "ramo", "rosado", "M", True, "primavera"],
    "FLO2": ["Caja Elegante", "caja", "blanco", "L", True, "todo año"],
    "FLO3": ["Ramo Solar", "ramo", "amarillo", "S", False, "verano"],
    "FLO4": ["Centro Mesa", "centro", "rojo", "M", True, "todo año"],
    "FLO5": ["Ramo Bosque", "ramo", "verde", "L", False, "otoño"],
    "FLO6": ["Caja Noche", "caja", "morado", "M", True, "invierno"]
}

# Diccionario con precio y stock
bodega = {
    "FLO1": [15990, 8],
    "FLO2": [29990, 3],
    "FLO3": [9990, 12],
    "FLO4": [24990, 5],
    "FLO5": [19990, 0],
    "FLO6": [22990, 6]
}

# ==========================
# FUNCIONES DE VALIDACIÓN
# ==========================

def validar_codigo(codigo):
    codigo = codigo.upper()

    if codigo.strip() == "":
        return False

    if codigo in arreglos:
        return False

    return True


def validar_nombre(nombre):
    if nombre.strip() == "":
        return False

    return True


def validar_tipo(tipo):
    if tipo.strip() == "":
        return False

    return True


def validar_color(color):
    if color.strip() == "":
        return False

    return True


def validar_tamano(tamano):
    tamano = tamano.upper()

    if tamano == "S" or tamano == "M" or tamano == "L":
        return True

    return False


def validar_tarjeta(tarjeta):
    tarjeta = tarjeta.lower()

    if tarjeta == "s" or tarjeta == "n":
        return True

    return False


def validar_temporada(temporada):
    if temporada.strip() == "":
        return False

    return True


def validar_precio(precio):
    if precio > 0:
        return True

    return False


def validar_unidades(unidades):
    if unidades >= 0:
        return True

    return False
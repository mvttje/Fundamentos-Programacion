
flores = {
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

def unidades_arreglo(tipo):
            
            total = 0

            for codigo in flores:

                if flores[codigo][1].lower() == tipo.lower():
                    
                    total += bodega[codigo][1]
                
            print("El total de unidades disponibles es: ",total)

def buscar_precio(minimo,maximo):
    resultados = []
    for codigo,dato in bodega.items():
         if bodega[precio][1] == minimo or maximo:
              precio = bodega[0]
              unidades = bodega[1]
              if minimo >= 0 and maximo > 0 and minimo < maximo:
                   if codigo in flores:
                        nombre = flores[0]
                        resultados.append(f"{nombre}--{codigo}")

                   

     

     
def menu():
    while True:

        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por tipo de arreglo")
        print("2. Búsqueda de arreglos por rango de precio")
        print("3. Actualizar precio de arreglo")
        print("4. Agregar arreglo")
        print("5. Eliminar arreglo")
        print("6. Salir")
        print("=====================================")

        op = int(input("Opcion: "))

        if op == 1:

            tipo = input("Ingrese tipo de arreglo: ")

            unidades_arreglo(tipo)
        elif op == 2:
             
             while True:
                  try:
                       minimo = int(input("Ingresa el valor minimo: "))
                       maximo = int(input("Ingresae el valor maximo: "))
                       if minimo and maximo > 1:
                            break
                       else:
                            print("Debes ingresar un numero valido")
                  except:
                       print("Debes ingresar un numero valido")
             buscar_precio(minimo,maximo)
             break
        

if __name__ == "__main__":
    menu()
    
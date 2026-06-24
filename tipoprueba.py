
#funciones2.py

#Con Argumento y con retorno
def suma(a,b):
    suma = (a + b)
    return suma

#Con argumento sin retorno
def nombre_seleccion(seleccion):
    print("La seleccion es: ",seleccion)
    
#Sin argumento y sin retorno
def mostrar_favorito():
    print("Favoritos para ganar el mundial")
    print("Argentina")
    print("Brasil")
    print("Francias")

#Sin argumento y con retorno
def cantidad_equipos():
    cantidad = 48
    return cantidad


def main():
    mostrar_favorito()
    equipos = cantidad_equipos()
    print("Cantidad de equipos: ",equipos)
    seleccion = input("Ingrese una seleccion: ")
    nombre_seleccion(seleccion)
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    resultado = suma(a,b)
    print(resultado)
    
if __name__ == "__main__":
    main()
#Aqui trabajaremos funciones

def funcion_sencilla():
    print("Hola, Soy el papichulo")
funcion_sencilla()

def suma():
    num1 = 2
    num2 = 6
    return(num1 + num2)
print("La suma es: ",suma())

def resta():
    num1 = 10
    num2 = 5
    return(num1 - num2)
print("la resta es: ",resta())

def suma(a,b):
    sumar = a+b
    print(f"La suma de los argumentos es: {sumar}")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
suma(num1,num2)
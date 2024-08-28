# a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo
# que numero = 10:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# En el programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro numero.
# ii. Debe validarse que el dato ingresado por el usuario corresponda a
# un dígito, y no a otro tipo de dato como un carácter.
# iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for,
# while).
# BONUS: Luego, codificar una función equivalente que utilice recursividad.


def suma(numero):
    suma_acum = 0
    for n in range(1, numero + 1):
        suma_acum += n
    return suma_acum

def es_numero(numero):
    return numero.isdigit()

def validar_numero():
    while True:
        numero = input("Ingrese un número entero: ")
        if es_numero(numero):
            return int(numero)
        else:
            print("Por favor, ingrese un número válido (número entero).")

# Llamada principal
numero = validar_numero()
print(f"La suma de 1 hasta {numero} es: {suma(numero)}")










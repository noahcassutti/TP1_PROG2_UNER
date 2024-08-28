# . Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de
# números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista
# e imprima ambas. La lista de números la ingresa el usuario en forma de números
# separados por coma.
# Suponiendo que el usuario ingresa la siguiente lista:
# 1,2,3,4,5,6,7,8,9
# Entonces, la salida del programa debería ser:
# 2,4,6,8
# 1,9,25,49,81

def numeros_par_impar(entrada):
    
    entrada = entrada.replace(' ', '').replace('.', ',')
    lista_numeros = entrada.split(',')
    
    lista_pares = []
    lista_impares_al_cuadrado = []
    
    
    for numero in lista_numeros:
        numero = int(numero)

        if numero % 2 == 0: 
            lista_pares.append(numero)
        else:  
            cuadrado = numero * numero 
            lista_impares_al_cuadrado.append(cuadrado)

    
    print("Números pares:", lista_pares)
    print("Impares ingresados  al cuadrado:", lista_impares_al_cuadrado)


def main():
    while True:
        opcion = int(input("Ingrese cualquier numero para ingresar (con 0 finaliza): "))

        if opcion == 0:
            print("Gracias por participar!")
            break 
        entrada = input("Ingrese una lista de números separados por coma: ")
        numeros_par_impar(entrada)

if __name__ == "__main__": 
    main()
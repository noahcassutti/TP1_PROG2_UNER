# . Escriba un procedimiento procesar_palabras(entrada) que acepte una
# secuencia de palabras separadas por coma, las ordene y las imprima.
# Suponiendo que la entrada provista al programa es la siguiente:
# te,felicito,que,bien,actuas
# La salida esperada es:
# actuas,bien,felicito,que,te

def procesar_palabras(entrada):
    palabras = entrada.split(',')
    palabras.sort()
    for palabra in palabras:
        print(palabra, end=', ')


def main():
    while True:
        opcion = int(input("\nIngrese cualquier numero para ingresar (con 0 finaliza): "))

        if opcion == 0:
            print("Gracias por participar!")
            break 
        entrada = input("Ingrese el texto: ")
        procesar_palabras(entrada)

if __name__ == "__main__": 
     main()
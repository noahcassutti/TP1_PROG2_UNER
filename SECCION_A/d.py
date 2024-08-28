# d. Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
# que tome ambas como parámetros e imprima dos listas, cada una con:
# i. Los elementos en común, en orden inverso.
# ii. Los elementos no comunes, en orden alfabético.
# El programa debería arrojar el siguiente resultado:
# listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# ['c', 'b']
# ['a', 'e', 'd']

def listas_diferencia(lista1, lista2): 
    
    # Encontrar elementos en común
    comun = [item for item in lista1 if item in lista2]
    comun = list(dict.fromkeys(comun))  # Eliminar duplicados
    comun.reverse()  # Ordenar en orden inverso
    
    # Encontrar elementos no comunes
    no_comun = [item for item in lista1 + lista2 if item not in comun]
    no_comun = list(dict.fromkeys(no_comun))  # Eliminar duplicados
    no_comun.sort()  # Ordenar alfabéticamente
    
    # Imprimir las listas
    print("elementos en común: ", comun)
    print("elementos que no tienen en comun: ", no_comun)

def main():
    while True:
        opcion = int(input("Ingrese cualquier numero para ingresar (con 0 finaliza): "))

        if opcion == 0:
            print("Gracias por participar!")
            break

        lista1 = input("Ingrese la primera lista: ")

        lista2 = input("Ingrese la segunda lista: ")

        list(lista1)
        list(lista2)

        listas_diferencia(lista1, lista2)
        
if __name__ == "__main__": 
     main()   


# b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y
# cuando las letras que componen dicha palabra estén en orden alfabético, y False
# en caso contrario.


def es_abc(palabra):
    for i in range(len(palabra) - 1): #recorre cada letra
        if palabra[i] > palabra[i + 1]: #verifica el orden y retorna true o false(si la letra es posterior)
            return False
    return True



def main():
    while True:
        opcion = int(input("Ingrese cualquier numero para ingresar (con 0 finaliza): "))

        if opcion == 0:
            print("Gracias por participar!")
            break 
        
        ingreso = input("Ingrese una palabra: ")
        print(es_abc(ingreso))

if __name__ == "__main__": 
     main()

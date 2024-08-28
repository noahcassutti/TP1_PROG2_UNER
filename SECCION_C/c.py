#c. Tal como sucede con la lógica proposicional, en Python muchas veces las
#expresiones booleanas pueden ser simplificadas manteniendo el valor de
#erdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente
#a a and b. A continuación, intente simplificar las siguientes expresiones y
#escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el
#valor de verdad de las expresiones ya simplificadas:
#i. (a or b) or (b and c)
#ii. b and c or False
#iii. a and b or c or (b and a)
#iv. a == True or b == False


def procesar_sentencias(a, b, c):
    
    # (a or b) or (b and c)
    # i. a or b
    resultado_sentencia_uno = a or b
    
    # b and c or False
    # ii. b and c
    resultado_sentencia_dos = b and c
    
    # a and b or c or (b and a)
    # iii: a and b or c
    resultado_sentencia_tres = a and b or c
    
    # a == True or b == False
    # iv: a or not b
    resultado_sentencia_cuatro = a or not b

    print("Resultado de la 1era expresión:", resultado_sentencia_uno)
    print("Resultado de la 2nda expresión:", resultado_sentencia_dos)
    print("Resultado de la 3era expresión:", resultado_sentencia_tres)
    print("Resultado de la 4rta expresión:", resultado_sentencia_cuatro)


def main():
    while True:
        opcion = int(input("Ingrese cualquier numero para ingresar (con 0 finaliza): "))

        if opcion == 0:
            print("Gracias por participar!")
            break 

        a = bool(int(input("Ingrese 1 para True, 0 para False (a): ")))
        b = bool(int(input("Ingrese 1 para True, 0 para False (b): ")))
        c = bool(int(input("Ingrese 1 para True, 0 para False (c): ")))
        procesar_sentencias(a, b, c)

if __name__ == "__main__":
    main()     

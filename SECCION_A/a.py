# Escribir una función de nombre palabra_no_tiene_letras(palabra,
# letras_prohibidas), la cual retorne True si es que los caracteres que componen
# una palabra no se encuentran en una lista de caracteres prohibidos.


#funcion de palabra no tiene letra, itinerando sobre el string palabra .
letras_prohibidas = ['w', 'b', 'i', 'h', 'o']
def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            print("Esta palabra no contiene letras prohibidas:") 
            return False
    if letra not in letras_prohibidas:
        print("Esta palabra  tiene letras prohibidas: ")
        return True 
#menu
def main():
    while True:

        opcion = int(input("Ingrese cualquier numero para ingresar (con 0 finaliza): "))

        if opcion == 0:
            print("Gracias por participar!")
            break
        
        palabra = input("Ingrese una palabra. Se dará como resultado True si no tiene letras prohibidas: ")
        print(palabra_no_tiene_letras(palabra, letras_prohibidas))
if __name__ == "__main__": 
     main()


   
    
    

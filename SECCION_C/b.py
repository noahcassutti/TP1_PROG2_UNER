# Escribir un programa que resuelva la secuencia de Fibonacci a pedido del
# usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro
# numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio
# anterior, validado. La función debe encargarse de calcular la secuencia para
# dicho número

num1 = 0
num2 = 1

def fibonacci(num): 
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2) #calcula el número como la suma de los dos anteriores
    


def main():
    while True:
        opcion = int(input("Ingrese cualquier numero para ingresar (con 0 finaliza): "))

        if opcion == 0:
            print("Gracias por participar!")
            break 
        
        while True:#tiene que ingresar un valor mayor o igual a 0
            try:
                n = int(input("Ingrese un número entero: "))
                if n >= 0:
                    break
                else:
                    print("El número debe ser mayor o igual a 0")
            except ValueError:
                print("Por favor ingrese un valor válido")

        for i in range(n):
            print(fibonacci(i)) 

if __name__ == "__main__": 
     main()

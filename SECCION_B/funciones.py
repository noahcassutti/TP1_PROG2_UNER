import time
from calendar import isleap


# calcular si es un año bisiesto
def anio_bisiesto(anio):
    return isleap(anio)

# calcular el numero de dias de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
    if  mes in [1,3,5,7,8,10,12]:
        return 31
    elif mes in [4,6,9,11]:
        return 30
    elif mes == 2 and anio_bisiesto == True:
        return 29
    elif mes == 2 and anio_bisiesto == False:
        return 28
    
def validar_edad():
    while True:
        edad = input("Ingrese su edad: ")
        try:
            anios = int(edad)  
            if anios < 0:
                print("La edad no puede ser negativa. Por favor, ingrese un número positivo.")
            else:
                return anios  
        except ValueError:
            print("Error: la edad ingresada debe ser un número entero. Inténtelo de nuevo.")
# encapsulado
def calcular_dias_edad(hora_local, anio_comienzo, anio_fin):

    
    dias = 0

    # Calcula los días de los años completos
    for a in range(anio_comienzo, anio_fin):
        if anio_bisiesto(a):
            dias += 366
        else:
            dias += 365

    # Añade los días transcurridos en el año actual
    for m in range(1, hora_local.tm_mon):
        dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))

    # Añade los días del mes actual
    dias += hora_local.tm_mday

    return dias
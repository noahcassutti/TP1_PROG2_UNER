from funciones import *

import time
from calendar import isleap

def main():
    # ingreso de datos del usuario
    nombre = input("Ingrese su nombre: ")
    edad = validar_edad()
    # seteo inicial de variables
    hora_local = time.localtime(time.time())
    anios = int(edad)
    anio_comienzo = int(hora_local.tm_year) - anios
    anio_fin = anio_comienzo + anios
    meses = anios * 12 + hora_local.tm_mon
    dias = calcular_dias_edad(hora_local, anio_comienzo, anio_fin)

    # imprimir la edad del usuario
    print("La edad de %s es %d años o " % (nombre, anios), end="")
    print("%d meses o %d días" % (meses, dias))

if __name__ == "__main__":
    main()
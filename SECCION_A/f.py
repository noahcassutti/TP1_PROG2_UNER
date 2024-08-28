# f. Un portal web requiere un formulario de alta de usuario donde se ingrese,
# mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python,
# una función contrasena_valida(contrasena) que devuelva True en caso de
# superar las siguientes validaciones sobre la contraseña proporcionada por el
# usuario:
# i. Longitud entre 6 y 20 caracteres.
# ii. Debe contener al menos un número.
# iii. Debe contener al menos dos mayúsculas.
# iv. Debe contener al menos un carácter especial.
# v. No puede contener espacios.
# La salida esperada es la siguiente:
# abc.123 es válida: False
# Abc.123 es válida: False
# AbC.123 es válida: True
# AbC.1 23 es válida: False
# ÁbC.123 es válida: False
# Para la búsqueda de caracteres de cierto tipo (mayúsculas, acentos, espacios y
# otros) debe hacerse uso de la librería re:
# - https://docs.python.org/es/3/library/re.html
# - https://relopezbriega.github.io/blog/2015/07/19/expresiones-regularescon-python/
# - Para buscar caracteres especiales, puede utilizarse la siguiente expresión
# [$&+,:;=?@#|<>.^*()%!-]


# Solicitar al usuario que ingrese usuario y contraseña a validar 
usuario = input("Ingrese usuario: ")
contraseña = input("Ingrese contraseña: ")

#importamos libreria Re
import re

# Función que valida la contraseña,segun requisitos especificos 
def contrasena_valida(contraseña):
    # longitud min 6 a 20 caracteres.
    if not (6 <= len(contraseña) <= 20):
        return False

    # números (se coloca para abreriar \d= [0-9],que busca cualquier digito)
    if not re.search(r'\d', contraseña):
        return False

    # dos mayúsculas que esten dentro del abecedario. 
    if len(re.findall(r'[A-Z]', contraseña)) < 2:
        return False

    # un carácter especial dentro del cochete
    if not re.search(r'[$&+,:;=?@#|<>.^*()%!-]', contraseña):
        return False

  # verifica que no haya espacios , utilizando el caracter \s que busca espacios
    if re.search(r'\s', contraseña):
        return False

    return True

# Validar la contraseña ingresada
validar = contrasena_valida(contraseña)

# resultado de la validación
if validar == True:
    print(f"La contraseña es válida: {validar}")
else:
    print(f"La contraseña no es válida: {validar}")